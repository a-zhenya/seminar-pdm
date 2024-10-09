from pytest import mark
from src.myproject9.task import add_two_numbers


@mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5)])
def test_add_two_numbers(a, b, expected):
    assert add_two_numbers(a, b) == expected, "Should return the sum of two numbers"
