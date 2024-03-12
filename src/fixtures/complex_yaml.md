# This is a text with JSON objects [1]

## Invalid markdown

```yaml
escapedBraces:
  '"{': '"}'
nested:
  array:
  - 1
  - 2
  - 3
  - key: value
  - ⍼
  - null
  - true
  - ©
  key: value
numbers:
- 30
- 40.3
string: John
'true': false
utf: New York
```

```yaml
- array first
- array second
- escapedBraces:
    '"{': '"}'
  nested:
    array:
    - 1
    - 2
    - 3
    - key: value
    - ⍼
    - null
    - true
    - ©
    key: value
  numbers:
  - 30
  - 40.3
  string: John
  'true': false
  utf: New York
```

```yaml
- random
- inline
- json
```

```yaml
also: random
```
