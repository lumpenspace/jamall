# jAMALL

jAMALL allows you to swap JSON into YAML for the benefit of LLMs and back again.

Additionally, it will store the content of incoming and outgoing JSON/YAML blocks into python objects.

## Features

- **Automatic Detection of JSON**: The `ConvertFromJson` class automatically detects JSON objects within the provided text, even if they are nested or formatted in various ways.
- **Conversion to YAML**: Converts detected JSON objects to YAML, preserving the structure and data types.
- **Markdown Code Block Support**: Encloses the YAML converted text in markdown code blocks, making it ready for documentation or markdown-based platforms.

By using the `ConvertFromJson` class, developers can streamline the process of converting JSON to YAML, enhancing the readability and usability of data when interacting with LLMs or for documentation purposes.

## Quickstart

(not yet on pypi, but you can install it from github)

```bash
## Install from github
pip install git+
pip install git git+https://github.com/lumpenspace/jamall.git
```

## Usage

The `ConvertFromJson` class converts JSON objects within a string to YAML format, and vice versa.

This conversion is particularly useful when working with LLMs (Large Language Models), as it allows for the easy interchange of data formats in a more human-readable form.

```python
from jamall import ConvertFromJson

messages=[{**message, "content": ConvertFromJson.from_text(message)} for message in messages];

client.chat_completion(
    messages=[{"role": "system", "content": ConvertFromJson.from_text(text_with_json)}],
)
```

## API

### ConvertFromJson

The `ConvertFromJson` class provides the following methods:

- `from_text(text: str) -> str`
  
  Initialises the class from a string containing JSON objects and converts them to YAML format.
- `__str__() -> str`
  
  Converts the stored JSON objects to YAML format and returns the result as a string.
- `__repr__() -> str`
  
  Returns the string representation of the class instance.
