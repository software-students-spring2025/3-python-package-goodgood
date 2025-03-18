import pytest
from src.palindrome import palindrome

def test_palindrome_true():
    assert palindrome("racecar") is True

def test_palindrome_false():
    assert palindrome("hello") is False

def test_palindrome_with_spaces():
    assert palindrome("nurses run") is True

def test_palindrome_false():
    assert palindrome("1881") is True

def test_palindrome_false():
    assert palindrome("Able was I ere I saw Elba") is True
