import pytest
from dotpath import dot_get

def test_dot_get_existing_path():
    data = {"user": {"profile": {"email": "test@example.com"}}}
    assert dot_get(data, "user.profile.email") == "test@example.com"
    
def test_dot_get_nonexistent_path_returns_default():
    data = {"user": {"profile": {}}}
    assert dot_get(data, "user.profile.name", default="Unknown") == "Unknown"

def test_dot_get_partial_missing_path_returns_default():
    data = {"user": {}}
    assert dot_get(data, "user.profile.email", default=None) is None

def test_dot_get_empty_path_returns_entire_dict():
    data = {"a": 1}
    assert dot_get(data, "") == data

def test_dot_get_midway_non_dict_returns_default():
    data = {"user": {"profile": "string_instead_of_dict"}}
    assert dot_get(data, "user.profile.email", default="missing") == "missing"

def test_dot_get_root_level_key():
    data = {"username": "neil"}
    assert dot_get(data, "username") == "neil"