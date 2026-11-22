import pytest

import orders


def test_line_total():
    assert orders.line_total(25, 4) == 100
    assert orders.line_total(19.99, 0) == 0


def test_line_total_rejects_negative_quantity():
    with pytest.raises(ValueError):
        orders.line_total(10, -1)


def test_order_total():
    assert orders.order_total([(50, 2), (100, 1)], discount_percent=50) == 118


def test_free_shipping_starts_at_the_threshold():
    assert orders.free_shipping([(250, 2)]) is True
    assert orders.free_shipping([(249, 2)]) is False
