# XDK Python SDK

<!--
Auto-generated README for the X API Python SDK.

This file contains the documentation and usage examples
for the generated Python SDK package.

Generated automatically - do not edit manually.
-->

A Python SDK for the X API.

## Installation

```bash
uv add xdk
```

Or with pip:
```bash
pip install xdk
```

## Usage

```python
from xdk import Client

# Initialize the client
client = Client(
    api_key="your_api_key",
    api_secret="your_api_secret",
    access_token="your_access_token",
    access_token_secret="your_access_token_secret"
)

# Use the client to interact with the X API
# For example, to get posts:
posts = client.posts.get(ids=["1234567890"])

# To search for posts:
search_results = client.posts.recent_search(query="python")

# To post a post:
post = client.posts.create(post_data={"text": "Hello, world!"})
```

## Features

- Full support for the X API v2
- Simple and intuitive interface
- Comprehensive documentation
- Type hints for better IDE support

## Documentation

For more information, see the [documentation](https://xdk.com/docs/python).

## License

This project is licensed under the MIT License - see the LICENSE file for details. 