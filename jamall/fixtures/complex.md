# This is a text with JSON objects [1]

## Invalid markdown

```json
    {
        "string": "John",
        "numbers": [30, 40.3],
        "true": false,
        "utf": "New York",
        "escapedBraces": { "\"{": "\"}" },
        "nested": {
            "key": "value",
            "array": [1, 2, 3, { "key": "value" }, "⍼", null, true, "\u00A9"]
        }
    }
```

This is a text with a YAML object

```yaml
ignore_me: good boy
name: John
age: 30
city: New York
```

```json
[
    "array first",
    "array second",
    {
        "string": "John",
        "numbers": [30, 40.3],
        "true": false,
        "utf": "New York",
        "escapedBraces": { "\"{": "\"}" },
        "nested": {
            "key": "value",
            "array": [1, 2, 3, { "key": "value" }, "⍼", null, true, "\u00A9"]
        }
    }
]
```

["random", "inline", "json"] {
    "also": "random"
}