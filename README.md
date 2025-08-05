# py-dotpath

**py-dotpath** is a tiny Python utility that lets you **safely get and set nested dictionary values** using simple dot notation paths.

Example:
```python
from dotpath import dot_get, dot_set

data = {"user": {"profile": {"email": "x@example.com"}}}
email = dot_get(data, "user.profile.email")  # returns 'x@example.com'

dot_set(data, "user.profile.name", "Bingus")
print(data)  # {'user': {'profile': {'email': 'x@example.com', 'name': 'Bingus'}}}
