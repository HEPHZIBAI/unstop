'''
Problem Statement
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

Input Format
First line contains the integer n.

Second line contains the integer k.

Output Format
Display the sum of digits after converting the number into base k.

Constraints
1 <= n <= 100
2 <= k <= 10
Sample Testcase 0
Testcase Input
10
10
Testcase Output
1
Explanation
n is already in base 10.


Sum of digits: 1 + 0 = 1.

Sample Testcase 1
Testcase Input
8
2
Testcase Output
1
Explanation
Number base 2 is : 1000


The sum of digits: 1+0+0+0 = 1
'''


n=int(input())
k=int(input())
converted_number = []
while n > 0:
  converted_number.append(n % k)
  n //= k
  #print(converted_number)
    
print(sum(converted_number))