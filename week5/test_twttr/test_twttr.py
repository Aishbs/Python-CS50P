from twttr import shorten
import pytest

def test_cases():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwitTer') == 'TwtTr'

def test_number():
    assert shorten('123') == '123'

def test_punctuation ():
    assert shorten('!$') == '!$'