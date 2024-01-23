# Given an integer N, write a program to count the number of digits in N.

# Input Format

# Example 1: Input0: N = 12345

# Example 2: Input1: N = 8394

# Constraints

# n <= 10000

# Output Format

# Output0: 5 Explanation: N has 5 digits

# Output1: 4 Explanation: N has 4 digits

# Sample Input 0

# 12345
# Sample Output 0

# 5
#approach 1
#count 
n=int(input())
count = 0
while n > 0:
    count = count + 1
    n = n//10
print(count)
#approach 2
#count 
n=int(input())
print(len(str(n)))