import emoji

"""
Enter the emotion and get a string with corresponding emoji at the end of the string. 

"""
def emoji(s->str, emotion->str) -> str: 
    if (emotion.casefold() == "happy".casefold()):
        return emoji.emojize(s + " :beaming_face_with_smiling_eyes: ")
    else if (emotion.casefold() == "friendly".casefold()):
        return emoji.emojize(s + " :grinning_face_with_big_eyes: ")
    else if (emotion.casefold() == "laughing".casefold()):
        return emoji.emojize(s + " :face_with_tears_of_joy: ")
    else if (emotion.casefold() == "love".casefold()):
        return emoji.emojize(s + " :smiling_face_with_heart_eyes: ")
    else if (emotion.casefold() == "numb".casefold()):
        return emoji.emojize(s + " :emotionless_face: ")
    else if (emotion.casefold() == "wordless".casefold()):
        return emoji.emojize(s + " :unamuzed_face: ")
    else if (emotion.casefold() == "surprise".casefold()):
        return emoji.emojize(s + " :exploding_head: ")
    else if (emotion.casefold() == "angry".casefold()):
        return emoji.emojize(s + " :enraged_face: ")
    else if (emotion.casefold() == "sad".casefold()):
        return emoji.emojize(s + " :loudly_crying_face: ")
    else if (emotion.casefold() == "cheated".casefold()):
        return emoji.emojize(s + " :clown_face: ")
    else: 
        return emoji.emojize(s + " :shushing_face: ")


