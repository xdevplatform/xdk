import os
import shutil
import subprocess
import sys
import json
import importlib
import pkgutil
from pathlib import Path

try:
    from markdownify import markdownify as html_to_md
except ImportError:
    html_to_md = None

ROOT = Path(__file__).resolve().parent
PKG_DIR = ROOT / "xdk"
DOCS_DIR = ROOT / "docs"
SPHINX_OUT = ROOT / "docs_html"
MINT_OUT = ROOT / "mintlify-docs" / "xdks"
NAV_JSON = ROOT / "mintlify-docs" / "python-sdk-navigation.json"


def generate_markdown_for_module(module_name: str) -> str:
    """Generate Markdown documentation for a module using pdoc's API."""
    try:
        import pdoc
        mod = importlib.import_module(module_name)
        # Try pdoc.doc.Module (pdoc 10.x - 16.x)
        try:
            doc = pdoc.doc.Module(mod)
            return doc.text()
        except (AttributeError, TypeError):
            pass
        # Try pdoc.Module (older versions)
        try:
            doc = pdoc.Module(mod)
            return doc.text()
        except (AttributeError, TypeError):
            pass
        # Try using pdoc's render module
        try:
            import pdoc.render
            return pdoc.render.text_module(mod)
        except (AttributeError, ImportError, TypeError):
            pass
        # Fallback: use subprocess to call pdoc CLI
        try:
            env = os.environ.copy()
            env["PYTHONPATH"] = f"{PKG_DIR.parent}:{env.get('PYTHONPATH','')}"
            result = subprocess.run(
                [sys.executable, "-m", "pdoc", "--text", module_name],
                capture_output=True,
                text=True,
                env=env,
                cwd=ROOT,
                timeout=30,
            )
            if result.returncode == 0:
                return result.stdout
        except Exception:
            pass
        return f"# {module_name}\n\nUnable to generate documentation with pdoc API."
    except Exception as e:
        return f"# {module_name}\n\nError generating documentation: {e}"


def discover_modules(package_name: str) -> list[str]:
    """Discover all modules in a package."""
    modules = []
    try:
        package = importlib.import_module(package_name)
        package_path = (
            Path(package.__file__).parent if hasattr(package, "__file__") else None
        )
        if package_path:
            for importer, modname, ispkg in pkgutil.walk_packages(
                [str(package_path)], prefix=f"{package_name}."
            ):
                if not modname.endswith(".pyc"):
                    modules.append(modname)
        # Also add the package itself if it has content
        modules.append(package_name)
    except Exception as e:
        print(f"Warning: Error discovering modules in {package_name}: {e}")
    return sorted(set(modules))


def run_sphinx() -> None:
    """Build HTML docs with Sphinx into docs_html."""
    SPHINX_OUT.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{PKG_DIR.parent}:{env.get('PYTHONPATH','')}"
    # Ensure Sphinx is available; user installs via Makefile target
    cmd = [sys.executable, "-m", "sphinx", "-b", "html", str(DOCS_DIR), str(SPHINX_OUT)]
    subprocess.run(cmd, check=True, cwd=ROOT, env=env)


def _classify_page(rel: Path) -> tuple[str, str]:
    """Return (group, title) for a given relative md path from pdoc."""
    parts = [p for p in rel.parts if p]
    stem = rel.stem
    # Clients: xdk/<tag>/client.md
    if len(parts) >= 3 and parts[0] == "xdk" and parts[-1] == "client.md":
        tag = parts[-2].replace("_", " ").title()
        return ("Clients", f"{tag} Client")
    # Models: xdk/<tag>/models.md
    if len(parts) >= 3 and parts[0] == "xdk" and parts[-1] == "models.md":
        tag = parts[-2].replace("_", " ").title()
        return ("Models", f"{tag} Models")
    # Pagination
    if parts[-1] == "paginator.md":
        return ("Pagination", "Pagination")
    # Authentication
    if parts[-1] in ("oauth2_auth.md",):
        return ("Authentication", "OAuth 2.0")
    # Top-level package index
    if parts[-1] in ("xdk.md",):
        return ("Overview", "Overview")
    # Utilities (fallback)
    title = stem.replace("_", " ").title()
    return ("Utilities", title)


def convert_to_mintlify() -> None:
    if MINT_OUT.exists():
        shutil.rmtree(MINT_OUT)
    MINT_OUT.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict]] = {}
    # Convert Sphinx HTML index to Overview MDX (embed HTML in MDX)
    xdk_html = SPHINX_OUT / "index.html"
    if xdk_html.exists():
        html_content = xdk_html.read_text(encoding="utf-8")
        # Convert HTML → Markdown if markdownify is available
        if html_to_md:
            md_content = html_to_md(html_content, heading_style="ATX")
        else:
            md_content = html_content
        out_path = MINT_OUT / "xdk" / "overview.mdx"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        frontmatter = "---\nsidebarTitle: Overview\n---\n\n"
        out_path.write_text(frontmatter + md_content, encoding="utf-8")
        grouped.setdefault("Overview", []).append(
            {
                "path": "/" + str(out_path.relative_to(MINT_OUT)).replace(os.sep, "/"),
                "title": "Overview",
            }
        )
    # Convert autosummary module pages to MDX (embed HTML in MDX)
    autosummary_dir = SPHINX_OUT / "_autosummary"
    if autosummary_dir.exists():
        for html_file in autosummary_dir.rglob("*.html"):
            rel_module = html_file.stem  # e.g., xdk.users.client
            if not rel_module.startswith("xdk"):
                continue
            parts = rel_module.split(".")
            out_rel = Path(*parts)
            out_path = (MINT_OUT / out_rel).with_suffix(".mdx")
            out_path.parent.mkdir(parents=True, exist_ok=True)
            html = html_file.read_text(encoding="utf-8")
            # Convert HTML → Markdown if markdownify is available
            if html_to_md:
                body = html_to_md(html, heading_style="ATX")
            else:
                body = html
            title = parts[-1].replace("_", " ").title()
            if parts[-1] == "client":
                group = "Clients"
                sidebar = f"{parts[-2].replace('_', ' ').title()} Client"
            elif parts[-1] == "models":
                group = "Models"
                sidebar = f"{parts[-2].replace('_', ' ').title()} Models"
            elif parts[-1] == "paginator":
                group = "Pagination"
                sidebar = "Pagination"
            elif parts[-1] in ("oauth2_auth",):
                group = "Authentication"
                sidebar = "OAuth 2.0"
            else:
                group = "Utilities"
                sidebar = title
            frontmatter = f"---\nsiderbarTitle: {sidebar}\n---\n\n"
            # Fix typo key if any
            frontmatter = frontmatter.replace("siderbarTitle", "sidebarTitle")
            out_path.write_text(frontmatter + body, encoding="utf-8")
            grouped.setdefault(group, []).append(
                {
                    "path": "/"
                    + str(out_path.relative_to(MINT_OUT)).replace(os.sep, "/"),
                    "title": sidebar,
                }
            )
    # Build a lightweight navigation file
    sections = []
    # Desired order similar to TS
    order = [
        "Overview",
        "Authentication",
        "Client",
        "Clients",
        "Pagination",
        "Streaming",
        "Models",
        "Utilities",
        "Other",
    ]
    for group in order:
        if group in grouped:
            pages = sorted(grouped[group], key=lambda p: p["title"].lower())
            sections.append({"group": group, "pages": pages})
    # Append any leftover groups
    for group, pages in grouped.items():
        if not any(s["group"] == group for s in sections):
            sections.append(
                {
                    "group": group,
                    "pages": sorted(pages, key=lambda p: p["title"].lower()),
                }
            )
    nav = {"title": "Python SDK", "sections": sections}
    NAV_JSON.parent.mkdir(parents=True, exist_ok=True)
    NAV_JSON.write_text(json.dumps(nav, indent=2), encoding="utf-8")


def main() -> None:
    run_sphinx()
    convert_to_mintlify()


if __name__ == "__main__":
    main()
