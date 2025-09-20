import argparse
from constants import (
    ALLOWED_CHARACTERS_FOR_FILENAME,
    ALLOWED_CHARACTERS_FOR_PREFIX,
    ALLOWED_FILE_EXTENSION_FOR_FILENAME,
    DEFAULT_LENGTH_OF_COUPON,
    DEFAULT_NUMBER_OF_COUPONS,
    MAX_LENGTH_OF_COUPON,
    MAX_NUMBER_OF_COUPONS,
    MIN_LENGTH_OF_COUPON,
    MIN_NUMBER_OF_COUPONS,
)


class ArgParser:
    def __init__(self):
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
            help=f"Prefix for the coupons. [Example: CS50, Allowed Prefix Characters: {ALLOWED_CHARACTERS_FOR_PREFIX}]",
        )
        parser.add_argument(
            "-s",
            "--save",
            dest="s",
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
        filename = args.s

        return {
            "number_of_coupons": number_of_coupons,
            "length_of_coupon": length_of_coupon,
            "prefix": prefix,
            "filename": filename,
        }
