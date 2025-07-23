from main import get_weather, add, sub, mul, div
import pytest

def test_get_weather():
    assert get_weather(30) == "Hot"
    assert get_weather(10) == "Cold"
    assert get_weather(20) == "Normal"

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(1, 2) == -1

def test_mul():
    assert mul(1, 2) == 2

def test_div():
    with pytest.raises(ValueError,match="Cannot divide by zero"):
        div(1, 0)
    assert div(10, 2) == 5
