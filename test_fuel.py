from fuel import convert, gauge
import pytest

def test_dividezero():
    with pytest.raises(ZeroDivisionError):
        convert('100/0')

def test_alphabet():
    with pytest.raises(ValueError):
        convert('a/b')

def test_convert():
    assert convert ('1/3') == 33

def test_E():
    assert gauge(1) == 'E'

def test_F():
    assert gauge(99) == 'F'

def test_percentage():
    assert gauge(50) == '50%'