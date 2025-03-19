def reverse(text: str) -> str:
    """
    Reverses every word in the given string.

    Example:
        "Hello, world!" → "world! Hello,"
    """
    string = text.split()
    reversed_string = string[::-1]
    return " ".join(reversed_string)