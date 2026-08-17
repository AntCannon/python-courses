import pytest
from main_05 import is_prime


# pytest.mark.parametrize(
# <str of comma separated parameters>,
# <list of tuples> -> [tuples]
# )
@pytest.mark.parametrize(
    "num, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (19, True),
        (25, False),
    ],
)
def test_is_prime(num, expected):
    assert is_prime(num) == expected
