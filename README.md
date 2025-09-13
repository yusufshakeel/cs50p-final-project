# couponpy

#### Video Demo:  <URL HERE>

#### Description:

**couponpy** is a Python program that helps you generate coupons.

It can generate 1 million coupons per execution and it is configurable.

#### Prerequisite

* Python >= 3.11
* Git

#### Getting started

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
```
Number of coupons to generate. [Min: 1, Max: 1000000, Default: 1]
```

* -l L, --length_of_coupon L
```
Length of coupon. [Min: 4, Max: 16, Default: 5]
```

* -s, --save
```
Save the coupons in file ./output/coupons.txt
```