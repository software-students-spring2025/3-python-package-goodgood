import re

def palindrome(text: str) -> bool:
    # checks if a string given is palindrome, meaning it reads the same forward and backward, 
    # case insensitive, ignores spaces, and returns bollean value.
    str_lower = text.lower()
    cleaned = re.sub(r'[^a-z0-9]', '', text)
    return cleaned == cleaned[::-1]