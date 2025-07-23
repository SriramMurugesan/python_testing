import pytest
from db import Database

@pytest.fixture
def db():
    """Fixture to create a database"""
    database=Database()
    yield database
    database.data.clear()


def test_add_user(db):
    assert db.add_user(1, "User 1") == True
    assert db.get_user(1) == "User 1"
    assert db.remove_user(1) == True
    with pytest.raises(ValueError,match="User does not exist"):
        db.remove_user(1)
        
def test_add_duplicate_user(db):
    assert db.add_user(1, "User 1") == True
    with pytest.raises(ValueError,match="User already exists"):
        db.add_user(1, "User 1")
    