import random
import os
import re
from typing import List, Set
from better_profanity import profanity

from argparser import ArgParser
from constants import (
    ALLOWED_CHARACTERS_FOR_FILENAME,
    ALLOWED_CHARACTERS_FOR_PREFIX,
    ALLOWED_CHARACTERS_FOR_SUFFIX,
    ALLOWED_FILE_EXTENSION_FOR_FILENAME,
    CHARACTER_SET,
    COUPON_PREFIX_ARGS_OPTIONS,
    COUPON_SUFFIX_ARGS_OPTIONS,
    FILE_ARGS_OPTIONS,
    LENGTH_OF_COUPON_ARGS_OPTIONS,
    MAX_LENGTH_OF_COUPON,
    MAX_LENGTH_OF_PREFIX,
    MAX_LENGTH_OF_SUFFIX,
    MAX_NUMBER_OF_COUPONS,
    MIN_LENGTH_OF_COUPON,
    MIN_NUMBER_OF_COUPONS,
    NUMBER_OF_COUPONS_ARGS_OPTIONS,
    OUTPUT_DIR,
)


os.makedirs(f"./{OUTPUT_DIR}", exist_ok=True)
profanity.load_censor_words()


def main():
    try:
        parser = ArgParser()
        args = parser.parse_args()

        number_of_coupons = args["number_of_coupons"]
        length_of_coupon = args["length_of_coupon"]
        prefix = args["prefix"]
        suffix = args["suffix"]
        filename = args["filename"]

        validate(number_of_coupons, length_of_coupon, prefix, suffix, filename)

        coupons = generate(number_of_coupons, length_of_coupon, prefix, suffix)

        if filename:
            filepath = f"./{OUTPUT_DIR}/{filename}"
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
    suffix: str = "",
    filename: str = "",
) -> None:
    if number_of_coupons > MAX_NUMBER_OF_COUPONS:
        raise ValueError(
            f"{NUMBER_OF_COUPONS_ARGS_OPTIONS} cannot be greater than {MAX_NUMBER_OF_COUPONS}"
        )
    elif number_of_coupons < MIN_NUMBER_OF_COUPONS:
        raise ValueError(
            f"{NUMBER_OF_COUPONS_ARGS_OPTIONS} cannot be less than {MIN_NUMBER_OF_COUPONS}"
        )

    if length_of_coupon > MAX_LENGTH_OF_COUPON:
        raise ValueError(
            f"{LENGTH_OF_COUPON_ARGS_OPTIONS} cannot be greater than {MAX_LENGTH_OF_COUPON}"
        )
    elif length_of_coupon < MIN_LENGTH_OF_COUPON:
        raise ValueError(
            f"{LENGTH_OF_COUPON_ARGS_OPTIONS} cannot be less than {MIN_LENGTH_OF_COUPON}"
        )

    length_of_prefix = len(prefix)
    if length_of_prefix:
        if length_of_prefix > MAX_LENGTH_OF_PREFIX:
            raise ValueError(
                f"{COUPON_PREFIX_ARGS_OPTIONS} cannot have more than {MAX_LENGTH_OF_PREFIX} character(s)"
            )

        pattern = f"^{ALLOWED_CHARACTERS_FOR_PREFIX}+$"
        found = re.search(pattern, prefix)
        if found is None:
            raise ValueError(
                f"{COUPON_PREFIX_ARGS_OPTIONS} must only use the following characters {ALLOWED_CHARACTERS_FOR_PREFIX}"
            )

    length_of_suffix = len(suffix)
    if length_of_suffix:
        if length_of_suffix > MAX_LENGTH_OF_SUFFIX:
            raise ValueError(
                f"{COUPON_SUFFIX_ARGS_OPTIONS} cannot have more than {MAX_LENGTH_OF_SUFFIX} character(s)"
            )

        pattern = f"^{ALLOWED_CHARACTERS_FOR_SUFFIX}+$"
        found = re.search(pattern, suffix)
        if found is None:
            raise ValueError(
                f"{COUPON_SUFFIX_ARGS_OPTIONS} must only use the following characters {ALLOWED_CHARACTERS_FOR_SUFFIX}"
            )

    if len(filename):
        pattern = f"^{ALLOWED_CHARACTERS_FOR_FILENAME}+\\.{ALLOWED_FILE_EXTENSION_FOR_FILENAME}$"
        found = re.search(pattern, filename)
        if found is None:
            raise ValueError(
                f"{FILE_ARGS_OPTIONS} must only use the following characters {ALLOWED_CHARACTERS_FOR_FILENAME} and file extension {ALLOWED_FILE_EXTENSION_FOR_FILENAME}"
            )


def generate(
    number_of_coupons: int,
    number_of_chars_in_a_coupon: int,
    prefix: str = "",
    suffix: str = "",
) -> Set[str]:
    coupons: Set[str] = set()

    while len(coupons) < number_of_coupons:
        random_chars_for_coupon: List[str] = random.choices(
            CHARACTER_SET, k=number_of_chars_in_a_coupon
        )
        generated_coupon = prefix + "".join(random_chars_for_coupon) + suffix
        if not profanity.contains_profanity(generated_coupon):
            coupons.add(generated_coupon)

    return coupons


def save(coupons: List[str], filepath: str):
    with open(filepath, "w") as f:
        for coupon in coupons:
            f.write(f"{coupon}\n")


if __name__ == "__main__":
    main()
