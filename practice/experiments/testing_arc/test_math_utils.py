import pytest
import requests
from math_utils import add, safe_divide, Accumulator
from api_client import get_user_name


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

@pytest.fixture
def acc():
    return Accumulator()

def test_first_accumulator(acc):
    acc.add(5)
    assert acc.total == 5

def test_second_accumulator(acc):
    acc.add(10)
    assert acc.total == 10


class FakeResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        return self._json
    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} error")


def test_get_user_name(monkeypatch):
    # 🅰 ARRANGE — build a fake get() that ignores the URL and returns what we want
    def fake_get(url):
        return FakeResponse({"name": "Cal"})
    monkeypatch.setattr("api_client.requests.get", fake_get)   # ← splice the fake at the seam

    # 🅰 ACT
    result = get_user_name(99)

    # 🅰 ASSERT — your code parsed the fake correctly
    assert result == "Cal"

def test_get_user_name_404_raises(monkeypatch):
    def fake_get(url):
        return FakeResponse({"error": "not found"}, status_code=404)
    monkeypatch.setattr("api_client.requests.get", fake_get)

    with pytest.raises(requests.exceptions.HTTPError):
        get_user_name(99)