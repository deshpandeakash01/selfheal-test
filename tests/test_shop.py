import pytest

import shop


def test_subtotal():
    assert shop.subtotal([10, 20, 30]) == 60
    assert shop.subtotal([]) == 0


def test_apply_discount():
    assert shop.apply_discount(200, 10) == 180
    assert shop.apply_discount(200, 0) == 200


def test_apply_discount_rejects_bad_percent():
    with pytest.raises(ValueError):
        shop.apply_discount(100, 150)


def test_add_tax():
    assert shop.add_tax(100) == 118
    assert shop.add_tax(100, rate=0) == 100


def test_total():
    assert shop.total([100, 100], discount_percent=50) == 118
