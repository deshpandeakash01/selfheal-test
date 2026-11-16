"""Orders: lines of (unit price, quantity), priced with shop.py."""

import shop

FREE_SHIPPING_FROM = 500


def line_total(unit_price, quantity):
    """Price of one order line: unit price times quantity."""
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    return round(unit_price * quantity, 2)


def order_total(lines, discount_percent=0, tax_rate=shop.DEFAULT_TAX_RATE):
    """Total of an order, with discount and tax applied by shop.total."""
    return shop.total([line_total(p, q) for p, q in lines], discount_percent, tax_rate)


def free_shipping(lines, threshold=FREE_SHIPPING_FROM):
    """Shipping is free when the lines add up to the threshold or more."""
    return sum(line_total(p, q) for p, q in lines) >= threshold
