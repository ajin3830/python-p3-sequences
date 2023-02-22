#!/usr/bin/env python3

# seq = []
# def print_fibonacci(n):
#     seq.append(n)  
#     # pass
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return print_fibonacci(n-1) + print_fibonacci(n-2)

# print(print_fibonacci(9))

# Fn = Fn-1 + Fn-2

def print_fibonacci(length):
    fibonacci_sequence = []
    if length > 0:
        fibonacci_sequence.append(0)
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                # when we pass 3 as length, because i initially is 2
                i = 2
                # while 2 < 3 is true, we can execute loop body
                while i < length:
                    # the sum of [2-1] and [2-2] 
                    # gets appended to the end of sequence
                    fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
                    i += 1

    print(fibonacci_sequence)
# print(print_fibonacci(3))


# w/ range
# range is exclusive, range(2, length) -> 2 through length-1
# def print_fibonacci(length):
#     pass
#     fibonacci_sequence = []
#     if length > 0:
#         fibonacci_sequence.append(0)
#         if length > 1:
#             fibonacci_sequence.append(1)
#             if length > 2:
#                 for i in range(2, length):
#                     fibonacci_sequence.append(
#                         fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

#     print(fibonacci_sequence)