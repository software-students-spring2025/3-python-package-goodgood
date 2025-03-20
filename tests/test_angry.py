import pytest
from src.angry import angry

ANGRY_DB = [
    "@#!", "!!@", "%$#@", "!&*@", "#$%@", "!!@#", "@*&!", "#%!$", "$#!!", "@!#",
    "!!%#", "#@$", "^*!@", "!@*&", "@#!%", "%#!!", "$*!^", "!@#*&", "@%$", "#!!"
]

def test_angry_sentence():
    """Should add symbol sequences and exclamation marks at the end of the text"""
    angry_text = angry("I am very upset")
    
    assert angry_text.endswith("!!!")
    assert any(symbol in angry_text for symbol in ANGRY_DB)

def test_angry_single_word():
    """Should only add exclamation marks at the end of the single-word sentence"""
    angry_text = angry("No")

    assert(angry_text == "No!!!")

def test_invalid_string_throws_error():
    """Should raise TypeError when text is not a string"""
    invalid_text = 123

    with pytest.raises(TypeError):
        angry(invalid_text)