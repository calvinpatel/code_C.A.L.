# test_math_utils.py
from math_utils import add, safe_divide

def test_add_positives():
    result = add(2, 3)
    assert result == 5

def test_add_strings():
    result = add("ha", "ha")
    assert result == "haha"

def test_safe_divide():
    result = safe_divide(10, 0)
    assert result == 0