from setuptools import setup, find_packages

setup(
    name="xdk",
    version="0.1.0",
    description="Python SDK for the X API",
    author="XDK Team",
    author_email="info@xdk.com",
    url="https://github.com/xdk/xdk-python",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "requests-oauthlib>=1.3.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
