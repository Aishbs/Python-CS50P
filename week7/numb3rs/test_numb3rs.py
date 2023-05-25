from numb3rs import validate
import pytest

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("cat") == False
    assert validate("1.2.3.512") == False
    assert validate("512.1.2.3") == False
    assert validate("1.2.512.3") == False
    assert validate("1.512.2.3") == False
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True

    