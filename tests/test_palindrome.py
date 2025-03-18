import pytest
from src.palindrome import palindrome

def test_palindrome_true():
    assert palindrome("racecar") is True

def test_palindrome_false():
    assert palindrome("hello") is False

def test_palindrome_with_spaces():
    assert palindrome("nurses run") is True