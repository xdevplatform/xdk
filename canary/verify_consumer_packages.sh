#!/usr/bin/env bash
# Black-box consumer package installation smoke test across all 4 XDK SDKs:
#   1. Python:     build `.whl`, install into a clean isolated venv, verify imports + public/auth behavior
#   2. TypeScript: `npm pack` `.tgz`, install into a clean project, verify strict `tsc`, ESM `import`, and CJS `require`
#   3. Java:       `mvn install` `com.x:xdk`, compile & run a standalone Maven consumer using `try (XClient client = ...)`
#   4. C#:         `dotnet pack` `XDevPlatform.Xdk`, add `.nupkg` from local feed into `dotnet new console`, build & run
#
# Usage:
#   ./canary/verify_consumer_packages.sh [--live]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
XDK_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKSPACE_DIR="$(cd "$XDK_ROOT/.." && pwd)"

PYTHON_DIR="${PYTHON_DIR:-$WORKSPACE_DIR/xdk-python}"
TYPESCRIPT_DIR="${TYPESCRIPT_DIR:-$WORKSPACE_DIR/xdk-typescript}"
JAVA_DIR="${JAVA_DIR:-$WORKSPACE_DIR/xdk-java}"
CSHARP_DIR="${CSHARP_DIR:-$WORKSPACE_DIR/xdk-csharp}"

LIVE_MODE="0"
if [[ "${1:-}" == "--live" ]]; then
  LIVE_MODE="1"
fi

WORK="$(mktemp -d "${TMPDIR:-/tmp}/xdk-consumer-smoke.XXXXXX")"
trap 'rm -rf "$WORK"' EXIT

mkdir -p "$WORK"/{py-dist,py-app,ts-app,java-app/src/main/java/demo,cs-feed,cs-app}

echo "==> [1/4] Verifying Python wheel (xdk) in isolated consumer venv..."
(
  cd "$PYTHON_DIR"
  uv build --out-dir "$WORK/py-dist" -q
)
uv venv "$WORK/py-app/.venv" -q
uv pip install --python "$WORK/py-app/.venv/bin/python" "$WORK"/py-dist/*.whl -q
LIVE_MODE="$LIVE_MODE" "$WORK/py-app/.venv/bin/python" -c '
import http.server, json, os, socketserver, threading
import xdk
from xdk import Client, OAuth1, OAuth2PKCEAuth, schemas

seen_headers = {}

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        seen_headers[self.path] = dict(self.headers)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        body = json.dumps({"openapi": "3.0.3", "paths": {}}).encode()
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        pass

with socketserver.TCPServer(("127.0.0.1", 0), Handler) as httpd:
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    # Even when bearer_token is configured, public security:[] endpoint must NOT attach Authorization
    c = Client(base_url=f"http://127.0.0.1:{port}", bearer_token="placeholder-token")
    spec = c.general.get_open_api_spec()
    assert "Authorization" not in seen_headers["/2/openapi.json"], f"Unexpected Authorization header: {seen_headers}"
    httpd.shutdown()

if os.environ.get("LIVE_MODE") == "1":
    live_client = Client(bearer_token="placeholder-token")
    live_spec = live_client.general.get_open_api_spec()
    dumped = live_spec.model_dump() if hasattr(live_spec, "model_dump") else live_spec
    assert "openapi" in dumped and len(dumped.get("paths", {})) >= 200
print("    OK: Python wheel installed cleanly and passed consumer checks.")
'

echo "==> [2/4] Verifying TypeScript tarball (@xdevplatform/xdk) in isolated ESM + CJS + strict tsc app..."
(
  cd "$TYPESCRIPT_DIR"
  npm run build --silent
  npm pack --pack-destination "$WORK/ts-app" --silent >/dev/null
)
cat > "$WORK/ts-app/package.json" << 'EOF'
{
  "name": "xdk-ts-consumer-smoke",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "devDependencies": {
    "typescript": "^5.7.0",
    "@types/node": "^20.0.0"
  }
}
EOF
cat > "$WORK/ts-app/tsconfig.json" << 'EOF'
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "noEmit": true
  },
  "include": ["app.ts"]
}
EOF
cat > "$WORK/ts-app/app.ts" << 'EOF'
import { Client, OAuth1, OAuth2, type Users } from "@xdevplatform/xdk";

// Zero-arg constructor must compile under strict TypeScript
const anonClient = new Client();
const configuredClient = new Client({ bearerToken: "placeholder-token" });

export async function verifyTypes(): Promise<Users.GetByUsernameResponse | null> {
  void anonClient;
  void configuredClient;
  void OAuth1;
  void OAuth2;
  return null;
}
EOF
(
  cd "$WORK/ts-app"
  npm install ./xdevplatform-xdk-*.tgz --no-audit --no-fund --silent
  npx tsc -p tsconfig.json
  LIVE_MODE="$LIVE_MODE" node --input-type=module -e '
    import http from "node:http";
    import { createRequire } from "node:module";
    import { Client, OAuth1, OAuth2 } from "@xdevplatform/xdk";

    // Verify CJS entrypoint
    const requireCjs = createRequire(import.meta.url);
    const cjs = requireCjs("@xdevplatform/xdk");
    if (!cjs.Client || !cjs.OAuth1 || !cjs.OAuth2) {
      throw new Error("Missing CJS exports on @xdevplatform/xdk");
    }

    // Verify zero-arg constructor & security:[] header omission over local TCP
    let capturedAuth = undefined;
    const srv = http.createServer((req, res) => {
      capturedAuth = req.headers["authorization"];
      res.writeHead(200, { "content-type": "application/json" });
      res.end(JSON.stringify({ openapi: "3.0.3", paths: {} }));
    });
    await new Promise((r) => srv.listen(0, "127.0.0.1", r));
    const port = srv.address().port;
    try {
      const zeroArg = new Client();
      if (!zeroArg.general) throw new Error("Missing general client on zero-arg Client");
      const client = new Client({ baseUrl: `http://127.0.0.1:${port}`, bearerToken: "placeholder-token" });
      await client.general.getOpenApiSpec();
      if (capturedAuth !== undefined) {
        throw new Error(`Expected no Authorization header on /2/openapi.json, got: ${capturedAuth}`);
      }
    } finally {
      srv.close();
    }

    if (process.env.LIVE_MODE === "1") {
      const liveClient = new Client({ bearerToken: "placeholder-token" });
      const liveSpec = await liveClient.general.getOpenApiSpec();
      if (!liveSpec || typeof liveSpec !== "object" || !liveSpec.openapi) {
        throw new Error("Invalid live OpenAPI response");
      }
    }
    console.log("    OK: TypeScript tarball passed strict tsc, ESM, CJS, and runtime checks.");
  '
)

echo "==> [3/4] Verifying Java artifact (com.x:xdk) in standalone Maven consumer project..."
JAVA_VERSION="$(sed -n 's|^    <version>\(.*\)</version>$|\1|p' "$JAVA_DIR/pom.xml" | head -n 1)"
(
  cd "$JAVA_DIR"
  mvn -B -q install -DskipTests
)
cat > "$WORK/java-app/pom.xml" << EOF
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>demo</groupId>
  <artifactId>xdk-java-consumer-smoke</artifactId>
  <version>1.0.0</version>
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
  </properties>
  <dependencies>
    <dependency>
      <groupId>com.x</groupId>
      <artifactId>xdk</artifactId>
      <version>${JAVA_VERSION}</version>
    </dependency>
  </dependencies>
</project>
EOF
cat > "$WORK/java-app/src/main/java/demo/App.java" << 'EOF'
package demo;

import com.sun.net.httpserver.HttpServer;
import com.x.xdk.XClient;
import com.x.xdk.XClientConfig;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.atomic.AtomicReference;

public final class App {
    public static void main(String[] args) throws Exception {
        AtomicReference<String> seenAuth = new AtomicReference<>();
        HttpServer server = HttpServer.create(new InetSocketAddress("127.0.0.1", 0), 0);
        server.createContext(
                "/2/openapi.json",
                exchange -> {
                    seenAuth.set(exchange.getRequestHeaders().getFirst("Authorization"));
                    byte[] payload = "{\"openapi\":\"3.0.3\",\"paths\":{}}".getBytes(StandardCharsets.UTF_8);
                    exchange.getResponseHeaders().add("Content-Type", "application/json");
                    exchange.sendResponseHeaders(200, payload.length);
                    try (OutputStream os = exchange.getResponseBody()) {
                        os.write(payload);
                    }
                });
        server.start();
        try {
            int port = server.getAddress().getPort();
            try (XClient zeroArg = new XClient();
                    XClient client =
                            new XClient(
                                    XClientConfig.builder()
                                            .baseUrl("http://127.0.0.1:" + port)
                                            .bearerToken("placeholder-token")
                                            .build())) {
                if (zeroArg.general() == null) {
                    throw new IllegalStateException("Missing general() on zero-arg XClient");
                }
                var spec = client.general().getOpenApiSpec();
                if (spec == null || !spec.has("openapi")) {
                    throw new IllegalStateException("Invalid loopback OpenAPI spec");
                }
                if (seenAuth.get() != null) {
                    throw new IllegalStateException(
                            "Expected null Authorization on public endpoint, got: " + seenAuth.get());
                }
            }
        } finally {
            server.stop(0);
        }

        if ("1".equals(System.getenv("LIVE_MODE"))) {
            try (XClient live = new XClient(XClientConfig.builder().bearerToken("placeholder-token").build())) {
                var liveSpec = live.general().getOpenApiSpec();
                if (liveSpec == null || !liveSpec.has("openapi")) {
                    throw new IllegalStateException("Invalid live OpenAPI spec");
                }
            }
        }
        System.out.println("    OK: Java com.x:xdk Maven artifact passed standalone consumer checks.");
    }
}
EOF
(
  cd "$WORK/java-app"
  LIVE_MODE="$LIVE_MODE" mvn -B -q compile exec:java -Dexec.mainClass=demo.App
)

echo "==> [4/4] Verifying C# NuGet package (XDevPlatform.Xdk) in standalone .NET 8 console project..."
CSHARP_VERSION="$(sed -n 's|.*<Version>\(.*\)</Version>.*|\1|p' "$CSHARP_DIR/src/Xdk/Xdk.csproj" | head -n 1)"
(
  cd "$CSHARP_DIR"
  dotnet pack src/Xdk/Xdk.csproj -c Release -o "$WORK/cs-feed" --nologo -v q
)
cat > "$WORK/cs-app/NuGet.Config" << EOF
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <clear />
    <add key="local-xdk" value="$WORK/cs-feed" />
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
  </packageSources>
</configuration>
EOF
cat > "$WORK/cs-app/ConsumerSmoke.csproj" << EOF
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="XDevPlatform.Xdk" Version="${CSHARP_VERSION}" />
  </ItemGroup>
</Project>
EOF
cat > "$WORK/cs-app/Program.cs" << 'EOF'
using System.Net;
using System.Net.Sockets;
using System.Text;
using Xdk;

var listener = new TcpListener(IPAddress.Loopback, 0);
listener.Start();
var port = ((IPEndPoint)listener.LocalEndpoint).Port;
string? requestHead = null;

var serverTask = Task.Run(async () =>
{
    using var tcp = await listener.AcceptTcpClientAsync();
    using var stream = tcp.GetStream();
    var buf = new byte[4096];
    var n = await stream.ReadAsync(buf);
    requestHead = Encoding.UTF8.GetString(buf, 0, n);
    var body = "{\"openapi\":\"3.0.3\",\"paths\":{}}";
    var resp = $"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {body.Length}\r\nConnection: close\r\n\r\n{body}";
    var respBytes = Encoding.UTF8.GetBytes(resp);
    await stream.WriteAsync(respBytes);
});

try
{
    using var client = new XClient(new XClientOptions
    {
        BaseUrl = $"http://127.0.0.1:{port}",
        BearerToken = "placeholder-token",
    });
    var spec = await client.General.GetOpenApiSpecAsync();
    await serverTask;
    if (spec is null || !spec.ContainsKey("openapi"))
    {
        throw new InvalidOperationException("Invalid loopback OpenAPI spec");
    }
    if (requestHead is not null && requestHead.Contains("Authorization:", StringComparison.OrdinalIgnoreCase))
    {
        throw new InvalidOperationException($"Expected no Authorization header on public endpoint, got:\n{requestHead}");
    }
}
finally
{
    listener.Stop();
}

if (Environment.GetEnvironmentVariable("LIVE_MODE") == "1")
{
    using var liveClient = new XClient(new XClientOptions { BearerToken = "placeholder-token" });
    var liveSpec = await liveClient.General.GetOpenApiSpecAsync();
    if (liveSpec is null || !liveSpec.ContainsKey("openapi"))
    {
        throw new InvalidOperationException("Invalid live OpenAPI spec");
    }
}

Console.WriteLine("    OK: C# XDevPlatform.Xdk NuGet package passed standalone consumer checks.");
EOF
(
  cd "$WORK/cs-app"
  LIVE_MODE="$LIVE_MODE" dotnet run -c Release --nologo
)

echo "All 4 SDK consumer package installation & runtime checks passed!"
