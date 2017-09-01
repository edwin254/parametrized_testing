import pytest
from numberWork import runOddEvenCheck


@pytest.mark.parametrize("test_input,expected", [
    (3, "odd"),
    (4, "even"),
    (9, "even"),
])
def test_even_and_odd_numbers(test_input, expected):
    assert (runOddEvenCheck(test_input)) == expected
