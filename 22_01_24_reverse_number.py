# Given a number N reverse the number and print it.

# Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

# Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

# Input Format

# 123

# Constraints

# N <= 1000

# Output Format

# 321

#approach 1
#reverse number
n = int(input())
reverse_number = 0
while n > 0:
    a = n%10
    reverse_number = reverse_number * 10 + a
    n = n//10
print(reverse_number)

#approach 2
#reverse number
n = int(input())
b =str(n)
reverse_string = (b[::-1])
print(reverse_string)
