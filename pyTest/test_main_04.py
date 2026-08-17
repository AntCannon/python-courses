import pytest
from main_04 import Database


@pytest.fixture
def db():
    """Provides a fresh instance of the Database class and cleans up after the test"""
    database = Database()
    yield database  # provide the fixture instance
    database.data.clear()  # Cleanup step after all tests finish. Not needed for in-memory but useful for real DBs)


def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"


def test_add_duplicate_user_id(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User ID already exists"):
        db.add_user(1, "John")


def test_add_duplicate_user_name(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User Name already exists"):
        db.add_user(2, "Alice")


def test_del_user(db):
    db.add_user(1, "Alice")
    db.delete_user(1)
    with pytest.raises(ValueError, match="User does not exist"):
        db.get_user(1)
