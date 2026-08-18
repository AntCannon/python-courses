import pytest
from main_03 import UserManager


# fixtures run before every test
@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManger before each test."""
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"


def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "johnemail2@example.com")


# if you don't use a fixture and use a global variable a previous test can interfere with a succeeding test.

user_manager_global = UserManager()


def test_add_user_global():
    assert user_manager_global.add_user("john_doe", "john@example.com") == True
    assert user_manager_global.get_user("john_doe") == "john@example.com"


def test_add_duplicate_user_global(user_manager):
    user_manager_global.add_user("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager_global.add_user("john_doe", "johnemail2@example.com")
