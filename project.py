import argparse

DEFAULT_NUMBER_OF_COUPONS = 1
MAX_NUMBER_OF_COUPONS = 10000
DEFAULT_NUMBER_OF_COUPON_CHARACTERS = 5
MAX_NUMBER_OF_COUPON_CHARACTERS = 16
CHARACTER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        type=int,
        default=DEFAULT_NUMBER_OF_COUPONS,
        help=f"Number of coupons to generate. [Max: {MAX_NUMBER_OF_COUPONS}, Default: {DEFAULT_NUMBER_OF_COUPONS}]",
    )
    parser.add_argument(
        "-l",
        type=int,
        default=DEFAULT_NUMBER_OF_COUPON_CHARACTERS,
        help=f"Number of characters in a coupon. [Max: {MAX_NUMBER_OF_COUPON_CHARACTERS}, Default: {DEFAULT_NUMBER_OF_COUPON_CHARACTERS}]",
    )
    args = parser.parse_args()
    print(args)


def validate(): ...


def generate(): ...


def save(): ...


if __name__ == "__main__":
    main()
