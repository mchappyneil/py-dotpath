from typing import Any, Dict, Optional

def dot_get(data: Dict, path: str, default: Optional[Any] = None) -> Any:
    """
    Safely retrieves a value from a nested dictionary using dot notation.
    
    Args:
        data (dict): The dictionary to traverse.
        path (str): Dot-separated path string (e.g., "user.profile.email").
        default (Any, optional): Value to return if path does not exist.
        
    Returns:
        Any: The value at the specified path, or default if the path doesn't 
        exist.
    """
    if not path:
        return data
    
    current = data
    for key in path.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    
    return current

def dot_set(data: Dict, path: str, value: Any) -> Dict:
    """
    Sets a value inside a nested dictionary using dot notation.

    Args:
        data (dict): The dictionary to modify.
        path (str): Dot-separated path string (e.g., "user.profile.email").
        value (Any): The value to set.

    Returns:
        dict: The modified dictionary (same object, updated).
    """
    if not path:
        raise ValueError("Path cannot be empty.")

    keys = path.split(".")
    current = data
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value
    return data
