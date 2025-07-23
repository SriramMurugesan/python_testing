from main import get_weather, add, sub, mul, div, UserManager
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

@pytest.fixture
def user_manager():
    """Fixture to create a user manager"""
    return UserManager()

def test_user_manager(user_manager):
    assert user_manager.add_user(1, "User 1") == True
    assert user_manager.get_user(1) == "User 1"
    assert user_manager.remove_user(1) == True
    with pytest.raises(ValueError,match="User does not exist"):
        user_manager.remove_user(1)
    
def test_add_duplicate_user(user_manager):
    assert user_manager.add_user(1, "User 1") == True
    with pytest.raises(ValueError,match="User already exists"):
        user_manager.add_user(1, "User 1")