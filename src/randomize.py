import random

def randomize(text: str) -> str:
    """
    Randomly rearranges the letters in a given string, keeping spaces and punctuation in place.

    Example:
        "Hello, World!" -> "WeHll, oorld!"
    """
    letters = [char for char in text if char.isalpha()]  # Extract letters
    random.shuffle(letters)  # Shuffle letters randomly
    
    result = []
    letter_index = 0

    for char in text:
        if char.isalpha():
            result.append(letters[letter_index])
            letter_index += 1
        else:
            result.append(char)  # Keep punctuation and spaces in place
    
    return "".join(result)

# Example usage
print(randomize("Hello, World!"))
