'''
Problem 1: Counting Iron Man's Suits

Count the elements in the list

Iterative - Time O(n), Space O(1) - counter variable 
Recursive - Time O(n), Space O(n) - recursive call stack
'''
def count_suits_iterative(suits):
    count = 0
    for i in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

'''
Problem 2: Collecting Infinity Stones

Add elements in the array

Time - O(n), Space - O(n)
'''
def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

'''
Problem 3: Counting Unique Suits

Count non-repeating/unique elements in the list

Iterative - Time O(n), Space - O(1)
Recursive - Time O(n^2) - each recursive call - checking for dup, Space - O(n)
'''

def count_suits_iterative(suits):
    s = set(suits)
    count = 0
    for i in s:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    first = suits[0]
    if first in suits[1:]:
        return count_suits_recursive(suits[1:])
    else:
        return 1 + count_suits_recursive(suits[1:])

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

'''
Problem 4: Calculating Groot's Growth

Fibinocci series
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1

Time - O(2^n) exponential growth (worse than quadratic growth)
Space - O(n) - recursion stack
''' 

def fibonacci_growth(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

print(fibonacci_growth(5))
print(fibonacci_growth(8))

'''
Problem 5: Calculating the Power of the Fantastic Four

4 power n

Time - O(n) - makes one recursive call per unit
Space - O(n) - recursion stack
'''

def power_of_four(n):
    if n == 0:
        return 1
    elif n > 0:
        return 4 * power_of_four(n - 1)
    else:
        return 1 / (4 * power_of_four(-n - 1))

print(power_of_four(2))
print(power_of_four(-2))

'''
Problem 6: Strongest Avenger

max in the list

Time - 
'''

def strongest_avenger(strengths):
    if len(strengths) == 1:
        return strengths[0]
    else:
        max_of_rest = strongest_avenger(strengths[1:])
        return strengths[0] if strengths[0] > max_of_rest else max_of_rest

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))