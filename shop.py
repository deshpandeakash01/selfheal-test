"""A tiny shop-basket module.

It exists only so that its CI can be broken on purpose and the self-healing
agent can be tried on a repository where nothing valuable can be damaged.
"""

DEFAULT_TAX_RATE = 0.18


def subtotal(prices):
    """Sum of the item prices."""
    return sum(prices)


def apply_discount(amount, percent):
    """Reduce amount by percent (0 to 100): 200 less 10 percent is 180."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(amount * (100 - percent) / 100, 2)


def add_tax(amount, rate=DEFAULT_TAX_RATE):
    """Add tax at the given rate (0.18 = 18%): 100 becomes 118."""
    return round(amount * (1 + rate), 2)


def total(prices, discount_percent=0, tax_rate=DEFAULT_TAX_RATE):
    """Basket total: discount first, then tax."""
    return add_tax(apply_discount(subtotal(prices), discount_percent), tax_rate)
