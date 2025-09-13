import argparse
from typing import List, Set
import random

MIN_NUMBER_OF_COUPONS = 1
MAX_NUMBER_OF_COUPONS = 10000
DEFAULT_NUMBER_OF_COUPONS = 1
MIN_LENGTH_OF_COUPON = 4
MAX_LENGTH_OF_COUPON = 16
DEFAULT_LENGTH_OF_COUPON = 5
CHARACTER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
OUTPUT_FILENAME = "coupons.txt"


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-n",
            "--number_of_coupons",
            dest="n",
            type=int,
            default=DEFAULT_NUMBER_OF_COUPONS,
            help=f"Number of coupons to generate. [Min: {MIN_NUMBER_OF_COUPONS}, Max: {MAX_NUMBER_OF_COUPONS}, Default: {DEFAULT_NUMBER_OF_COUPONS}]",
        )
        parser.add_argument(
            "-l",
            "--length_of_coupon",
            dest="l",
            type=int,
            default=DEFAULT_LENGTH_OF_COUPON,
            help=f"Length of coupon. [Min: {MIN_LENGTH_OF_COUPON}, Max: {MAX_LENGTH_OF_COUPON}, Default: {DEFAULT_LENGTH_OF_COUPON}]",
        )
        parser.add_argument(
            "-s",
            "--save",
            dest="s",
            action="store_true",
            help=f"Save the coupons in file {OUTPUT_FILENAME}",
        )
        args = parser.parse_args()

        number_of_coupons = args.n
        number_of_chars_in_a_coupon = args.l

        validate(number_of_coupons, number_of_chars_in_a_coupon)

        coupons = generate(number_of_coupons, number_of_chars_in_a_coupon)

        if args.s:
            save(coupons)
            print(f"💾 Saved {number_of_coupons} coupon(s) in file {OUTPUT_FILENAME}")
        else:
            for coupon in coupons:
                print(coupon)
    except Exception as e:
        print(e)


def validate(number_of_coupons: int, number_of_chars_in_a_coupon: int) -> None:
    if number_of_coupons > MAX_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be greater than {MAX_NUMBER_OF_COUPONS}")
    elif number_of_coupons < MIN_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be less than {MIN_NUMBER_OF_COUPONS}")

    if number_of_chars_in_a_coupon > MAX_LENGTH_OF_COUPON:
        raise ValueError(f"l cannot be greater than {MAX_LENGTH_OF_COUPON}")
    elif number_of_chars_in_a_coupon < MIN_LENGTH_OF_COUPON:
        raise ValueError(f"l cannot be less than {MIN_LENGTH_OF_COUPON}")


def generate(number_of_coupons: int, number_of_chars_in_a_coupon: int) -> Set[str]:
    coupons: Set[str] = set()

    while len(coupons) < number_of_coupons:
        random_chars_for_coupon: List[str] = random.choices(
            CHARACTER_SET, k=number_of_chars_in_a_coupon
        )
        coupons.add("".join(random_chars_for_coupon))

    return coupons


def save(coupons: List[str]):
    with open(f"./{OUTPUT_FILENAME}", "w") as f:
        for coupon in coupons:
            f.write(f"{coupon}\n")


if __name__ == "__main__":
    main()
