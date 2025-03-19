import pytest
from uselessString import emoji
import random
import emoji


class Tests: 

    @pytest.fixture
    def example_fixture(self):
        emotion_list = ["happy", "friendly", "laughing", "laugh", "numb", "wordless", "surprise", "angry", "sad", "cheated", " "]
        emotion = random.choice(emotion_list)
        s = "Hello, World!"
        input = s, emotion
        return input
    
    def test_sanity_check(self, example_fixture): 
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_emotion(self, example_fixture): 
        for i in range(100): 
            actual = emoji(example_fixture)
            assert isinstance(
                actual, str
            ), f"Expected emoji() to return a string. Instead, it return {actual}"
            assert (
                len(actual) > 0
            ), f"Expected emoji() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_content(self, example_fixture): 
        assert (
            s, emotion = example_fixture
            actual = emoji(example_fixture)
            if (emotion == "happy"):
                expected = emoji.emojize(s + " :beaming_face_with_smiling_eyes: ")
                actual == expected
            else if (emotion == "friendly"):
                expected = s + " :grinning_face_with_big_eyes: "
                actual == expected
            else if (emotion == "laughing"):
                expected = emoji.emojize(s + " :face_with_tears_of_joy: ")
                actual == expected
            else if (emotion == "love"):
                expected = emoji.emojize(s + " :smiling_face_with_heart_eyes: ")
                actual == expected
            else if (emotion == "numb"):
                expected =  emoji.emojize(s + " :emotionless_face: ")
                actual == expected
            else if (emotion == "wordless"):
                expected = emoji.emojize(s + " :unamuzed_face: ")
                actual == expected
            else if (emotion == "surprise"):
                expected = emoji.emojize(s + " :exploding_head: ")
                actual == expected
            else if (emotion == "angry"):
                expected = emoji.emojize(s + " :enraged_face: ")
                actual == expected
            else if (emotion == "sad"):
                expected = emoji.emojize(s + " :loudly_crying_face: ")
                actual == expected
            else if (emotion == "cheated"):
                expected = emoji.emojize(s + " :clown_face: ")
                actual == expected
            else: 
                expected = emoji.emojize(s + " :shushing_face: ")
                actual == expected
        )f"Expected the string returned by emoji() to be with emotion {emotion}. Instead, it returned '{actual}'"