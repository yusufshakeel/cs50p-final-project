import pytest
from project import validate, generate, save


def test_validate():
    assert validate(1, 5) == None


def test_validate_should_raise_ValueError_when_n_is_less_than_1():
    with pytest.raises(ValueError) as e:
        validate(-1, 10)

    assert str(e.value) == "n cannot be less than 1"


def test_validate_should_raise_ValueError_when_n_is_greater_than_1000000():
    with pytest.raises(ValueError) as e:
        validate(10000000, 10)

    assert str(e.value) == "n cannot be greater than 1000000"


def test_validate_should_raise_ValueError_when_l_is_less_than_4():
    with pytest.raises(ValueError) as e:
        validate(10, 1)

    assert str(e.value) == "l cannot be less than 4"


def test_validate_should_raise_ValueError_when_l_is_greater_than_16():
    with pytest.raises(ValueError) as e:
        validate(10, 10000)

    assert str(e.value) == "l cannot be greater than 16"


def test_generate():
    coupons = generate(1, 5)
    assert len(coupons) == 1
    for coupon in coupons:
        assert coupon.isalnum() == True


def test_generate_n_coupons_have_l_characters():
    coupons = generate(3, 4)
    assert len(coupons) == 3
    for coupon in coupons:
        assert coupon.isalnum() == True


def test_save():
    coupons = ["CS50X", "CS50P"]
    save(coupons)
    with open("coupons.txt", "r") as f:
        for i, coupon in enumerate(f):
            assert coupon.strip() == coupons[i]
