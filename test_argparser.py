import sys
from argparser import ArgParser


def test_parse(monkeypatch):
    test_args = [
        "project.py",
        "-n",
        "3",
        "-l",
        "5",
        "-p",
        "CS50",
        "-s",
        "2025",
        "-f",
        "coupons.txt",
    ]
    monkeypatch.setattr(sys, "argv", test_args)

    parser = ArgParser()
    args = parser.parse_args()

    assert args == {
        "number_of_coupons": 3,
        "length_of_coupon": 5,
        "prefix": "CS50",
        "suffix": "2025",
        "filename": "coupons.txt",
    }
