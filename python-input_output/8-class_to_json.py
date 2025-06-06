def class_to_json(obj):
    """
    Returns dictionary description of an object for JSON serialization
    Args:
        obj: instance of a Class
    Returns:
        dictionary with simple data structure
    """
    return obj.__dict__
