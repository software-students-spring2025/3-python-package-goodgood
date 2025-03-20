# Import all functions from the package
from src.angry import angry
from src.echo import echo
from src.emotive import emotive
from src.mocking import mocking  
from src.palindrome import palindrome
from src.randomize import randomize
from src.reverse import reverse

def main():
    test_string = "Hello, World!"
    test_word = "Python"

    print("\n📌 Original String:", test_string, "\n")

    # Palindrome function (Reverses characters in the string)
    print("🔄 Palindrome:", palindrome(test_string))

    # Reverse function (Reverses word order)
    print("🔄 Reverse Words:", reverse(test_string))

    # Echo function (Repeats the word multiple times)
    print("🔊 Echo (3 times):", echo(test_word, 3))

    # Angry function (Adds rage sequences in between words and exclamation marks at the end)
    print("😡 Very Angry:", angry(test_string))

    # Mocking function (Alternates uppercase/lowercase)
    print("🃏 Mocking Case:", mocking(test_string))

    # Emotive function (Adds emotions to the string)
    print("😂 Add Emotion (Happy):", emotive(test_string, "happy"))

    # Randomize function (Shuffles characters in the string)
    print("🔀 Random Shuffle:", randomize(test_string))

    print("\n")

if __name__ == "__main__":
    main()
