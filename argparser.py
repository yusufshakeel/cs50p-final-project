import argparse
from constants import (
    ALLOWED_CHARACTERS_FOR_FILENAME,
    ALLOWED_CHARACTERS_FOR_PREFIX,
    ALLOWED_CHARACTERS_FOR_SUFFIX,
    ALLOWED_FILE_EXTENSION_FOR_FILENAME,
    COUPON_PREFIX_ARGS_LONG_OPTION,
    COUPON_PREFIX_ARGS_SHORT_OPTION,
    COUPON_SUFFIX_ARGS_LONG_OPTION,
    COUPON_SUFFIX_ARGS_SHORT_OPTION,
    DEFAULT_LENGTH_OF_COUPON,
    DEFAULT_NUMBER_OF_COUPONS,
    FILE_ARGS_LONG_OPTION,
    FILE_ARGS_SHORT_OPTION,
    LENGTH_OF_COUPON_ARGS_LONG_OPTION,
    LENGTH_OF_COUPON_ARGS_SHORT_OPTION,
    MAX_LENGTH_OF_COUPON,
    MAX_NUMBER_OF_COUPONS,
    MIN_LENGTH_OF_COUPON,
    MIN_NUMBER_OF_COUPONS,
    NUMBER_OF_COUPONS_ARGS_LONG_OPTION,
    NUMBER_OF_COUPONS_ARGS_SHORT_OPTION,
)


class ArgParser:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            NUMBER_OF_COUPONS_ARGS_SHORT_OPTION,
            NUMBER_OF_COUPONS_ARGS_LONG_OPTION,
            dest=NUMBER_OF_COUPONS_ARGS_SHORT_OPTION[1],
            type=int,
            default=DEFAULT_NUMBER_OF_COUPONS,
            help=f"Number of coupons to generate. [Min: {MIN_NUMBER_OF_COUPONS}, Max: {MAX_NUMBER_OF_COUPONS}, Default: {DEFAULT_NUMBER_OF_COUPONS}]",
        )
        parser.add_argument(
            LENGTH_OF_COUPON_ARGS_SHORT_OPTION,
            LENGTH_OF_COUPON_ARGS_LONG_OPTION,
            dest=LENGTH_OF_COUPON_ARGS_SHORT_OPTION[1],
            type=int,
            default=DEFAULT_LENGTH_OF_COUPON,
            help=f"Length of coupon. [Min: {MIN_LENGTH_OF_COUPON}, Max: {MAX_LENGTH_OF_COUPON}, Default: {DEFAULT_LENGTH_OF_COUPON}]",
        )
        parser.add_argument(
            COUPON_PREFIX_ARGS_SHORT_OPTION,
            COUPON_PREFIX_ARGS_LONG_OPTION,
            dest=COUPON_PREFIX_ARGS_SHORT_OPTION[1],
            type=str,
            default="",
            help=f"Prefix for the coupons. [Example: CS50, Allowed Prefix Characters: {ALLOWED_CHARACTERS_FOR_PREFIX}]",
        )
        parser.add_argument(
            COUPON_SUFFIX_ARGS_SHORT_OPTION,
            COUPON_SUFFIX_ARGS_LONG_OPTION,
            dest=COUPON_SUFFIX_ARGS_SHORT_OPTION[1],
            type=str,
            default="",
            help=f"Suffix for the coupons. [Example: 2025, Allowed Suffix Characters: {ALLOWED_CHARACTERS_FOR_SUFFIX}]",
        )
        parser.add_argument(
            FILE_ARGS_SHORT_OPTION,
            FILE_ARGS_LONG_OPTION,
            dest=FILE_ARGS_SHORT_OPTION[1],
            type=str,
            default="",
            help=f"Save the coupons in the provided filename. [Allowed Filename Characters: {ALLOWED_CHARACTERS_FOR_FILENAME}, File Extension: {ALLOWED_FILE_EXTENSION_FOR_FILENAME}]",
        )

        self._parser = parser

    def parse_args(self):
        args = self._parser.parse_args()
        number_of_coupons = args.n
        length_of_coupon = args.l
        prefix = args.p
        suffix = args.s
        filename = args.f

        return {
            "number_of_coupons": number_of_coupons,
            "length_of_coupon": length_of_coupon,
            "prefix": prefix,
            "suffix": suffix,
            "filename": filename,
        }
