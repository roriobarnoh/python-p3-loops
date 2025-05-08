#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        if i == 1:
            print("Happy New Year!")
        i -= 1
int_list = [1, 2, 3, 4, 5]
def square_integers(int_list):
    # code goes here!
    for i in range(len(int_list)):
        int_list[i] = int_list[i] **2

    return int_list

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
