#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length == 0:
        print([])
    else:
        fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233,377,610,987]
        
        newfib= list()
        for i in range(length):
            newfib.append(fib[i])
        print(newfib)