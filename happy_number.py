# '''
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# * Starting with any positive integer, replace the number by the sum of the squares of its digits.
# * Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a 
#   cycle which does not include 1.
# * Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# 2^2 = 4
# 4^2 = 16
# 1^2 + 6^2 = 37
# 3^2 + 7^2 = 58
# 5^2 + 8^2 = 89
# 8^2 + 9^2 = 145
# 1^2 + 4^2 + 5^2 = 42
# 4^2 + 2^2 = 20
# 2^2 + 0^2 = 4
# '''


def nextSquareSum(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit * digit
        n = n // 10
    return sum

def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = nextSquareSum(n)

    return n == 1

## Use Floyd's cycle-detection algorithm
def isHappy2(n):
    slow = n
    fast = nextSquareSum(n)
    
    while slow != fast:
        slow = nextSquareSum(slow)
        fast = nextSquareSum(nextSquareSum(fast))
        # slow在原本的位置走一步，fast在已經走一步之後再走兩步
    return slow == 1

print(f'Is 19 a happy number: {isHappy2(19)}')
print(f'Is 2 a happy number: {isHappy2(2)}')