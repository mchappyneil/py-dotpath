# py-dotpath

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![CI](https://github.com/mchappyneil/py-dotpath/actions/workflows/ci.yml/badge.svg)](https://github.com/mchappyneil/py-dotpath/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mchappyneil/py-dotpath/branch/main/graph/badge.svg?token=YOUR_CODECOV_TOKEN)](https://codecov.io/gh/mchappyneil/py-dotpath)


**py-dotpath** is a lightweight Python utility for safely and easily accessing and setting nested dictionary values using **dot notation paths**.

## ✨ Features
- Simple API: `dot_get()` and `dot_set()`.
- Automatically creates missing intermediate dictionaries.
- Safe traversal — avoids `KeyError` and `TypeError`.
- Zero dependencies, works on Python 3.7+.
- GPLv3 Licensed.

---

## 📦 Installation

```bash
pip install py-dotpath
```

## 🚀 Usage
```
from dotpath import dot_get, dot_set

data = {"user": {"profile": {"email": "x@example.com"}}}

# Get deeply nested values
email = dot_get(data, "user.profile.email")  
print(email)  # "x@example.com"

# Set values at any depth
dot_set(data, "user.profile.name", "John")
print(data)
# {"user": {"profile": {"email": "x@example.com", "name": "John"}}}

# Nonexistent paths are handled gracefully
nickname = dot_get(data, "user.profile.nickname", default="N/A")
print(nickname)  # "N/A"
```

## Why not just use `dict.get`?
The built-in `get()` works only at the first level:
```
data = {"user": {"profile": {"email": "x@example.com"}}}
data.get("user.profile.email")   # ❌ Always returns None
```
With **py-dotpath**, you can traverse nested dictionaries at any level:
```
dot_get(data, "user.profile.email")  # ✅ "x@example.com"
``` 

## 🤝 Contributing
- Fork the repo, create a branch, submit a PR.
- Run tests with `pytest`.
- Please include tests for new features.
