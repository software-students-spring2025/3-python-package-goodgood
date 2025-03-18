def palindrome(text: str) -> bool:
    # checks if a string given is palindrome, meaning it reads the same forward and backward, 
    # case insensitive and returns bollean value.
    str_lower = text.lower()
    return str_lower == str_lower[::-1]