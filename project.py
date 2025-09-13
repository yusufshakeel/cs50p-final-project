import argparse
import random
import os
import re
from typing import List, Set

MIN_NUMBER_OF_COUPONS = 1
MAX_NUMBER_OF_COUPONS = 1000000
DEFAULT_NUMBER_OF_COUPONS = 1
MIN_LENGTH_OF_COUPON = 4
MAX_LENGTH_OF_COUPON = 16
DEFAULT_LENGTH_OF_COUPON = 5
MAX_LENGTH_OF_PREFIX = 16
ALLOWED_CHARACTERS_FOR_PREFIX = "[A-Z0-9]"
CHARACTER_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
OUTPUT_DIR = "output"
OUTPUT_FILENAME = "coupons.txt"
OUTPUT_FILE_PATH = f"./{OUTPUT_DIR}/{OUTPUT_FILENAME}"

os.makedirs(f"./{OUTPUT_DIR}", exist_ok=True)


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
            "-p",
            "--prefix",
            dest="p",
            type=str,
            default="",
            help=f"Prefix for the coupons",
        )
        parser.add_argument(
            "-s",
            "--save",
            dest="s",
            action="store_true",
            help=f"Save the coupons in file {OUTPUT_FILE_PATH}",
        )
        args = parser.parse_args()

        number_of_coupons = args.n
        number_of_chars_in_a_coupon = args.l
        prefix = args.p

        validate(number_of_coupons, number_of_chars_in_a_coupon, prefix)

        coupons = generate(number_of_coupons, number_of_chars_in_a_coupon, prefix)

        if args.s:
            save(coupons)
            print(
                f"💾 Saved {number_of_coupons:,} coupon(s) in file {OUTPUT_FILE_PATH}"
            )
        else:
            for coupon in coupons:
                print(coupon)
    except Exception as e:
        print(e)


def validate(
    number_of_coupons: int, number_of_chars_in_a_coupon: int, prefix: str = ""
) -> None:
    if number_of_coupons > MAX_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be greater than {MAX_NUMBER_OF_COUPONS}")
    elif number_of_coupons < MIN_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be less than {MIN_NUMBER_OF_COUPONS}")

    if number_of_chars_in_a_coupon > MAX_LENGTH_OF_COUPON:
        raise ValueError(f"l cannot be greater than {MAX_LENGTH_OF_COUPON}")
    elif number_of_chars_in_a_coupon < MIN_LENGTH_OF_COUPON:
        raise ValueError(f"l cannot be less than {MIN_LENGTH_OF_COUPON}")

    number_of_chars_in_a_prefix = len(prefix)
    if number_of_chars_in_a_prefix:
        if number_of_chars_in_a_prefix > MAX_LENGTH_OF_PREFIX:
            raise ValueError(
                f"p cannot have more than {MAX_LENGTH_OF_PREFIX} character(s)"
            )

        pattern = f"^{ALLOWED_CHARACTERS_FOR_PREFIX}+$"
        found = re.fullmatch(pattern, prefix)
        if found is None:
            raise ValueError(
                f"p must only use the following characters {ALLOWED_CHARACTERS_FOR_PREFIX}"
            )


def generate(
    number_of_coupons: int, number_of_chars_in_a_coupon: int, prefix: str = ""
) -> Set[str]:
    coupons: Set[str] = set()

    while len(coupons) < number_of_coupons:
        random_chars_for_coupon: List[str] = random.choices(
            CHARACTER_SET, k=number_of_chars_in_a_coupon
        )
        coupons.add(prefix + "".join(random_chars_for_coupon))

    return coupons


def save(coupons: List[str]):
    with open(OUTPUT_FILE_PATH, "w") as f:
        for coupon in coupons:
            f.write(f"{coupon}\n")


if __name__ == "__main__":
    main()
