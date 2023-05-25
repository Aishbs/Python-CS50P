from bank import value
import pytest

def test_return_0():
    assert value('hello') == 0
    assert value('Hello, Aish') == 0
    assert value('HELLO') == 0
    assert value('HeLlO') == 0

def test_return_20():
    assert value('hi') == 20

def test_return_100():
    assert value('What\'s happening?') == 100