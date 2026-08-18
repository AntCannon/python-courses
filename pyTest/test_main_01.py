# from <file> import <function>
from pyTest.main_01 import get_weather


# create the test function test_<function>
def test_get_weather():
    # assert function / argument
    # <function(arg)> == <expected outcome>
    assert get_weather(21) == "hot"
    assert get_weather(19) == "cold"
