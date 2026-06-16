import pytest

# test_math_utils.py
from math_utils import add, safe_divide

def test_add_positives():
    result = add(2, 3)
    assert result == 5

def test_add_strings():
    result = add("ha", "ha")
    assert result == "haha"

def test_safe_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        safe_divide(10, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),       # ← look closely
    ("x", "y", "xy"),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected