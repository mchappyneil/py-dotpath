import pytest
from dotpath import dot_get, dot_set

# dot_get tests
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
    data = {"username": "mchappyneil"}
    assert dot_get(data, "username") == "mchappyneil"
    
# dot_set tests
def test_dot_set_creates_new_path():
    data = {}
    dot_set(data, "user.profile.email", "me@example.com")
    assert data == {"user": {"profile": {"email": "me@example.com"}}}

def test_dot_set_overwrites_existing_value():
    data = {"user": {"profile": {"email": "old@example.com"}}}
    dot_set(data, "user.profile.email", "new@example.com")
    assert data["user"]["profile"]["email"] == "new@example.com"

def test_dot_set_creates_intermediate_dicts():
    data = {"user": {}}
    dot_set(data, "user.profile.name", "Example")
    assert data == {"user": {"profile": {"name": "Example"}}}

def test_dot_set_non_dict_midway_is_overwritten():
    data = {"user": {"profile": "not_a_dict"}}
    dot_set(data, "user.profile.name", "Example")
    assert data == {"user": {"profile": {"name": "Example"}}}

def test_dot_set_returns_same_dict_instance():
    data = {}
    result = dot_set(data, "a.b.c", 123)
    assert result is data
