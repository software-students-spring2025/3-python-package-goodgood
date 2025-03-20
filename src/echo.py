def echo(text: str, num: int) -> str:
    """
    Repeats the given string the number of times provided

    Args:
        text (str): The text to be echoed/repeated.
        num (int): The number of times to echo/repeat the text.

    Returns:
        str: The text echoed/repeated the number of times indicated.
    """
    validate_echo_input(text, num)
    
    echoed_text = ""
    for i in range(num):
        echoed_text += text
    
    return echoed_text

def validate_echo_input(text: str, num: int) -> None:
    """
    Validates input for the echo() function.

    Args:
        text (str): The text input by the user.
        num (int): The number input by the user.
    
    Raises:
        TypeError: If `text` is not a string or `num` is not an integer.
        ValueError: If `num` is not a positive integer.
    """
    if not isinstance(text, str):
        raise TypeError("Invaid input: text must be a string.")
    if not isinstance(num, int):
        raise TypeError("Invalid input: number must be an integer.")
    
    if (num <= 0):
        raise ValueError("Invalid input: number must be a positive integer")