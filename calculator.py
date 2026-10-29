def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a percentage discount."""
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100")
    if price < 0:
        raise ValueError("Price cannot be negative")
    return price * (1 - discount_percent / 100)
