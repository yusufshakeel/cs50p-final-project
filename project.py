import argparse

MIN_NUMBER_OF_COUPONS = 1
MAX_NUMBER_OF_COUPONS = 10000
DEFAULT_NUMBER_OF_COUPONS = 1
MIN_NUMBER_OF_COUPON_CHARACTERS = 4
MAX_NUMBER_OF_COUPON_CHARACTERS = 16
DEFAULT_NUMBER_OF_COUPON_CHARACTERS = 5
CHARACTER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        type=int,
        default=DEFAULT_NUMBER_OF_COUPONS,
        help=f"Number of coupons to generate. [Min: {MIN_NUMBER_OF_COUPONS}, Max: {MAX_NUMBER_OF_COUPONS}, Default: {DEFAULT_NUMBER_OF_COUPONS}]",
    )
    parser.add_argument(
        "-l",
        type=int,
        default=DEFAULT_NUMBER_OF_COUPON_CHARACTERS,
        help=f"Number of characters in a coupon. [Min: {MIN_NUMBER_OF_COUPON_CHARACTERS}, Max: {MAX_NUMBER_OF_COUPON_CHARACTERS}, Default: {DEFAULT_NUMBER_OF_COUPON_CHARACTERS}]",
    )
    args = parser.parse_args()
    print(args)


def validate(number_of_coupons: int, number_of_chars_in_a_coupon: int) -> None:
    if number_of_coupons > MAX_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be greater than {MAX_NUMBER_OF_COUPONS}")
    elif number_of_coupons < MIN_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be less than {MIN_NUMBER_OF_COUPONS}")
    
    if number_of_chars_in_a_coupon > MAX_NUMBER_OF_COUPON_CHARACTERS:
        raise ValueError(f"l cannot be greater than {MAX_NUMBER_OF_COUPON_CHARACTERS}")
    elif number_of_chars_in_a_coupon < MIN_NUMBER_OF_COUPON_CHARACTERS:
        raise ValueError(f"l cannot be less than {MIN_NUMBER_OF_COUPON_CHARACTERS}")
    

def generate(): ...


def save(): ...


if __name__ == "__main__":
    main()
