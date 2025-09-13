# couponpy

#### Video Demo:  <URL HERE>

#### Description:

**couponpy** is a Python program that helps you generate coupons.

It can generate 1 million coupons per execution and it is configurable.

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

