def reverse(text: str) -> str:
    # reverses teh order of words in a given string
    string = text.split()
    reversed_string = string[::-1]
    return " ".join(reversed_string)