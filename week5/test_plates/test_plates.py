from plates import is_valid
import pytest

def test_code():
    assert is_valid("ABC10") == True
    assert is_valid("A") == False
    assert is_valid("ABC.12") == False
    assert is_valid("ABCDEF123") == False
    assert is_valid("ABC22A") == False
    assert is_valid("ABC01") == False
    assert is_valid("123ABC") == False
    assert is_valid("123") == False