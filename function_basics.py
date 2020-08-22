#!/usr/bin/env python


def say_hello():  # <1>
    print("Hello, world")
    print()
    # <2>


say_hello()  # <3>


def get_hello():
    return "Hello, world"  # <4>


h = get_hello()  # <5>
print(h)
print()


def sqrt(num):  # <6>
    return num ** .5


m = sqrt(1234)  # <7>
n = sqrt(2)

print("m is {:.3f} n is {:.3f}".format(m, n))

def sum_two_num(a,b):
    return (m+n)

print(sum_two_num(100,200))