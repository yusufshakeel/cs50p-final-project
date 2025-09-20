# couponpy

#### Video Demo:  https://www.youtube.com/watch?v=zayp4q4SHLA

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

##### Generate N coupons
* -n N, --number_of_coupons N
* Optional: True
* Default: 1
* Min: 1
* Max: 1000000

##### Generate coupon of length L
* -l L, --length_of_coupon L
* Optional: True
* Default: 5
* Min: 4
* Max: 16

##### Generate coupons with a prefix
* -p P, --prefix P
* Optional: True
* Allowed Prefix Characters: A-Z0-9
* Max length: 16
* Example: CS50

##### Generate coupons with a suffix
* -s S, --suffix S
* Optional: True
* Allowed Suffix Characters: A-Z0-9
* Max length: 16
* Example: 2025

##### Save coupons in a file
* -f F, --file F
* Optional: True
* Allowed Filename Characters: a-zA-Z0-9-_
* Allowed File Extension: txt|csv
* Example: coupons.txt

#### Examples

* Generate a coupon and log it to the console
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

* Generate coupons with suffix "2025"
```shell
➜ python project.py -s 2025
1AZ0X2025

➜ python project.py --suffix 2025
Z13DA2025
```

* Save coupons in a file
```shell
➜ python project.py -f coupons.txt
💾 Saved 1 coupon(s) in file ./output/coupons.txt

➜ python project.py --file coupons.txt
💾 Saved 1 coupon(s) in file ./output/coupons.txt
```
