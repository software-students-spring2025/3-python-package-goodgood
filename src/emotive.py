def emotive(s: str, emotion: str) -> str: 
    """
    Enter the emotion and get a string with corresponding emoji at the end of the string. 
    """
    if (emotion.casefold() == "happy".casefold()):
        emoji = "\U0001F601"
    elif (emotion.casefold() == "friendly".casefold()):
        emoji = "\U0001F603"
    elif (emotion.casefold() == "laughing".casefold()):
        emoji = "\U0001F602"
    elif (emotion.casefold() == "love".casefold()):
        emoji = "\U0001F60D"
    elif (emotion.casefold() == "numb".casefold()):
        emoji = "\U0001F611"
    elif (emotion.casefold() == "wordless".casefold()):
        emoji = "\U0001F612"
    elif (emotion.casefold() == "surprise".casefold()):
        emoji = "\U0001F92F"
    elif (emotion.casefold() == "angry".casefold()):
        emoji = "\U0001F621"
    elif (emotion.casefold() == "sad".casefold()):
        emoji = "\U0001F62D"
    elif (emotion.casefold() == "cheated".casefold()):
        emoji = "\U0001F921"
    else:
        emoji = "\U0001F92B"
    
    return (s + emoji)
    
    


