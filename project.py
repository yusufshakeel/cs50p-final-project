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
ALLOWED_CHARACTERS_FOR_FILENAME = "[a-zA-Z0-9-_]"
ALLOWED_FILE_EXTENSION_FOR_FILENAME = "(txt|csv)"

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
            type=str,
            default="",
            help=f"Save the coupons in the provided filename. [Allowed filename characters: {ALLOWED_CHARACTERS_FOR_FILENAME}, File Extension: {ALLOWED_FILE_EXTENSION_FOR_FILENAME}]",
        )
        args = parser.parse_args()

        number_of_coupons = args.n
        length_of_coupon = args.l
        prefix = args.p
        filename = args.s

        validate(number_of_coupons, length_of_coupon, prefix, filename)

        coupons = generate(number_of_coupons, length_of_coupon, prefix)

        if len(filename):
            filepath = f"./{OUTPUT_DIR}/{filename}"
        else:
            filepath = OUTPUT_FILE_PATH

        if args.s:
            save(coupons, filepath)
            print(f"💾 Saved {number_of_coupons:,} coupon(s) in file {filepath}")
        else:
            for coupon in coupons:
                print(coupon)
    except Exception as e:
        print(e)


def validate(
    number_of_coupons: int,
    length_of_coupon: int,
    prefix: str = "",
    filename: str = "",
) -> None:
    if number_of_coupons > MAX_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be greater than {MAX_NUMBER_OF_COUPONS}")
    elif number_of_coupons < MIN_NUMBER_OF_COUPONS:
        raise ValueError(f"n cannot be less than {MIN_NUMBER_OF_COUPONS}")

    if length_of_coupon > MAX_LENGTH_OF_COUPON:
        raise ValueError(f"l cannot be greater than {MAX_LENGTH_OF_COUPON}")
    elif length_of_coupon < MIN_LENGTH_OF_COUPON:
        raise ValueError(f"l cannot be less than {MIN_LENGTH_OF_COUPON}")

    length_of_prefix = len(prefix)
    if length_of_prefix:
        if length_of_prefix > MAX_LENGTH_OF_PREFIX:
            raise ValueError(
                f"p cannot have more than {MAX_LENGTH_OF_PREFIX} character(s)"
            )

        pattern = f"^{ALLOWED_CHARACTERS_FOR_PREFIX}+$"
        found = re.search(pattern, prefix)
        if found is None:
            raise ValueError(
                f"p must only use the following characters {ALLOWED_CHARACTERS_FOR_PREFIX}"
            )

    if len(filename):
        pattern = f"^{ALLOWED_CHARACTERS_FOR_FILENAME}+\\.{ALLOWED_FILE_EXTENSION_FOR_FILENAME}$"
        found = re.search(pattern, filename)
        if found is None:
            raise ValueError(
                f"s must only use the following characters {ALLOWED_CHARACTERS_FOR_FILENAME} and file extension {ALLOWED_FILE_EXTENSION_FOR_FILENAME}"
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


def save(coupons: List[str], filepath: str = OUTPUT_FILE_PATH):
    with open(filepath, "w") as f:
        for coupon in coupons:
            f.write(f"{coupon}\n")


if __name__ == "__main__":
    main()
