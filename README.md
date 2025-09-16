# couponpy

#### Video Demo:  <URL HERE>

#### Description:

**couponpy** is a Python program that helps you generate coupons.

It can generate 1 million coupons per execution and it is configurable.

#### Packages

This project uses the following packages.

| Name             | Purpose                              |
| ---------------- | ------------------------------------ |
| better-profanity | Check for profane words.             |
| black            | Used for code formatting.            |
| mypy             | For type checking.                   |
| pre_commit       | Manage and run Git pre-commit hooks. |
| pytest           | For testing.                         |

#### Prerequisite

* Python >= 3.11
* Git

#### Getting Started

* Clone the repository
```shell
git clone https://github.com/yusufshakeel/cs50p-final-project.git
```

* Setup virtual environment
```shell
python3 -m venv env
```

* Install the packages
```shell
pip install -r requirements.txt
```

* Usage
```shell
python project.py -h
```

#### Characters

This program uses the following characters `A-Z` and `0-9` to generate coupons.

#### Options

* -n N, --number_of_coupons N
  * Number of coupons to generate.
  * Optional: True
  * Default: 1
  * Min: 1
  * Max: 1000000

* -l L, --length_of_coupon L
  * Length of coupon.
  * Optional: True
  * Default: 5
  * Min: 4
  * Max: 16

* -p P, --prefix P
  * Prefix for the coupons.
  * Optional: True
  * Allowed Prefix Characters: A-Z0-9
  * Example: CS50

* -s S, --save S
  * Save the coupons in the provided filename.
  * Optional: True
  * Allowed Filename Characters: a-zA-Z0-9-_
  * Allowed File Extension: txt|csv
  * Example: coupons.txt

#### Examples

* Generate a single coupon and log on console
```shell
➜ python project.py
VG440
```

* Generate 3 coupons
```shell
➜ python project.py -n 3
GIAEA
5FKU4
Z50MX

➜ python project.py --number_of_coupons 3
E71UX
6BN3Y
6D74T
```

* Generate coupons of length 6
```shell
➜ python project.py -l 6
RCX5IA

➜ python project.py --length_of_coupon 6
WWOE19
```

* Generate coupons with prefix "CS50"
```shell
➜ python project.py -p CS50
CS50CHZ0B

➜ python project.py --prefix CS50
CS50JO4MG
```

* Save coupons in a file
```shell
➜ python project.py -s coupons.txt
💾 Saved 1 coupon(s) in file ./output/coupons.txt

➜ python project.py --save coupons.txt
💾 Saved 1 coupon(s) in file ./output/coupons.txt
```
