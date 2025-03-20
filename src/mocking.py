import random

def mocking(text: str) -> str:
    """
    Randomly changes the case of each letter in the given string.

    Example:
        "Hello, world!" -> "hEILo, WoRID!"
    """
    return "".join(
        char.upper() if random.choice([True, False]) else char.lower()
        for char in text
    )
