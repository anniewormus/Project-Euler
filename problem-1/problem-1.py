# Program by Annie Wormus 8.17.2023
"""
Problem 1 - Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
Loops through all numbers 1 - 1000 and adds them to sum if number is a multiple
of 3 or 5
Numbers that are multiples of both 3 and 5 are only added once
Runtime: O(n)
"""
def solution_1(limit):
    sum = 0
    for i in range(limit):
        if (i%3 == 0 or i%5 == 0):
            sum += i
    print(sum)

"""
Adds multiples to sum in increments of 3 and then increments of 5
Runtome: O(n/3)
"""
def solution_2(limit):
    sum = 0

    three_counter = 0
    while three_counter < limit:
        sum += three_counter
        three_counter += 3

    five_counter = 0
    while five_counter < limit:
        sum += five_counter
        five_counter += 5
        if five_counter % 3 == 0:
            five_counter += 5
    print(sum)

solution_1(1000)
solution_2(1000)