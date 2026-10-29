import pytest
from calculator import add, calculate_discount


def test_add_positive_numbers():
    assert add(10, 5) == 15


def test_add_negative_numbers():
    assert add(-3, -7) == -10


def test_calculate_discount_valid():
    # 20% off $100 should be $80
    assert calculate_discount(100.0, 20.0) == 80.0


def test_calculate_discount_full():
    # 100% off $50 should be free
    assert calculate_discount(50.0, 100.0) == 0.0


def test_calculate_discount_invalid_percent_raises_error():
    # Attempting a 150% discount should raise a ValueError
    with pytest.raises(ValueError, match="Discount percent must be between 0 and 100"):
        calculate_discount(100.0, 150.0)
