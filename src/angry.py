import random

def angry(text: str) -> str:
    """
    Adds expressive symbol sequences and exclamation marks at the end of the provided text.
    
    Args:
        text (str): The text to have the symbols and exclamation marks added to.
    
    Returns:
        str: The text modified with the symbols and exclamation marks.
    """
    validate_angry_input(text)

    angry_db = [
    "@#!", "!!@", "%$#@", "!&*@", "#$%@", "!!@#", "@*&!", "#%!$", "$#!!", "@!#",
    "!!%#", "#@$", "^*!@", "!@*&", "@#!%", "%#!!", "$*!^", "!@#*&", "@%$", "#!!"
]
    
    spaced_text = text.split(" ")
    angry_text = ""
    for i in range(len(spaced_text) - 1):
        angry_text += spaced_text[i] + " " + random.choice(angry_db) + " "
    
    angry_text += spaced_text[-1] + "!!!"

    return angry_text

def validate_angry_input(text: str) -> None:
    """
    Validates input for the angry() function.

    Args:
        text (str): The text input by the user.
    
    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Invaid input: text must be a string.")