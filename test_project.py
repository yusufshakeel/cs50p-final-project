import pytest
from project import validate, generate, save


def test_validate():
    assert validate(number_of_coupons=1, length_of_coupon=5) == None
    assert validate(number_of_coupons=1, length_of_coupon=5, prefix="CS50") == None
    assert (
        validate(number_of_coupons=1, length_of_coupon=5, prefix="CS50", suffix="2025")
        == None
    )
    assert (
        validate(
            number_of_coupons=1,
            length_of_coupon=5,
            prefix="CS50",
            suffix="2025",
            filename="output.txt",
        )
        == None
    )


def test_validate_should_raise_ValueError_when_n_is_less_than_1():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=-1, length_of_coupon=10)

    assert str(e.value) == "-n, --number_of_coupons cannot be less than 1"


def test_validate_should_raise_ValueError_when_n_is_greater_than_1000000():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=10000000, length_of_coupon=10)

    assert str(e.value) == "-n, --number_of_coupons cannot be greater than 1000000"


def test_validate_should_raise_ValueError_when_l_is_less_than_4():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=10, length_of_coupon=1)

    assert str(e.value) == "-l, --length_of_coupon cannot be less than 4"


def test_validate_should_raise_ValueError_when_l_is_greater_than_16():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=10, length_of_coupon=10000)

    assert str(e.value) == "-l, --length_of_coupon cannot be greater than 16"


def test_validate_should_raise_ValueError_when_p_has_more_than_16_char():
    with pytest.raises(ValueError) as e:
        validate(
            number_of_coupons=10,
            length_of_coupon=10,
            prefix="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

    assert str(e.value) == "-p, --prefix cannot have more than 16 character(s)"


def test_validate_should_raise_ValueError_when_p_has_invalid_characters():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=10, length_of_coupon=10, prefix="abc!@#$")

    assert (
        str(e.value) == "-p, --prefix must only use the following characters [A-Z0-9]"
    )


def test_validate_should_raise_ValueError_when_s_has_more_than_16_char():
    with pytest.raises(ValueError) as e:
        validate(
            number_of_coupons=10,
            length_of_coupon=10,
            suffix="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

    assert str(e.value) == "-s, --suffix cannot have more than 16 character(s)"


def test_validate_should_raise_ValueError_when_s_has_invalid_characters():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=10, length_of_coupon=10, suffix="abc!@#$")

    assert (
        str(e.value) == "-s, --suffix must only use the following characters [A-Z0-9]"
    )


def test_validate_should_raise_ValueError_when_f_has_invalid_characters():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=5, length_of_coupon=5, filename="hello$.txt")

    assert (
        str(e.value)
        == "-f, --file must only use the following characters [a-zA-Z0-9-_] and file extension (txt|csv)"
    )


def test_validate_should_raise_ValueError_when_f_has_invalid_file_extension():
    with pytest.raises(ValueError) as e:
        validate(number_of_coupons=5, length_of_coupon=5, filename="hello.pdf")

    assert (
        str(e.value)
        == "-f, --file must only use the following characters [a-zA-Z0-9-_] and file extension (txt|csv)"
    )


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


def test_generate_n_coupons_have_l_characters_with_prefix():
    coupons = generate(
        number_of_coupons=3, number_of_chars_in_a_coupon=4, prefix="CS50"
    )
    assert len(coupons) == 3
    for coupon in coupons:
        assert coupon.isalnum() == True
        assert len(coupon) == 8
        assert coupon[0:4] == "CS50"


def test_generate_n_coupons_have_l_characters_with_suffix():
    coupons = generate(
        number_of_coupons=3, number_of_chars_in_a_coupon=4, suffix="2025"
    )
    assert len(coupons) == 3
    for coupon in coupons:
        assert coupon.isalnum() == True
        assert len(coupon) == 8
        assert coupon[4:] == "2025"


def test_generate_n_coupons_have_l_characters_with_prefix_and_suffix():
    coupons = generate(
        number_of_coupons=3, number_of_chars_in_a_coupon=4, prefix="CS50", suffix="2025"
    )
    assert len(coupons) == 3
    for coupon in coupons:
        assert coupon.isalnum() == True
        assert len(coupon) == 12
        assert coupon[0:4] == "CS50"
        assert coupon[8:] == "2025"


def test_save():
    coupons = ["CS50X", "CS50P"]
    save(coupons, "./output/coupons.txt")
    with open("./output/coupons.txt", "r") as f:
        for i, coupon in enumerate(f):
            assert coupon.strip() == coupons[i]
