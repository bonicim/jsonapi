## Description

## Installation

### Development mode

In the root directory, run the following: `pip install -e .`

## Examples

```python
from jsonapi import jsonapi
cx_serialized = jsonapi.dumps(complex(1,2))
cx_deserialized = jsonapi.loads(cx_serialized)
```