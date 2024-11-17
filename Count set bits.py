'''
Problem Statement
Mohan gave Rohan a challenge. Mohan said “I will give you a number N. You have to convert each number from 1 to N into binary form (1's and 0's). Then, calculate the total number of occurence of 1 in those converted numbers.”

Rohan asks for your help in achieving this.

Input Format
You are given the integer N.

Output Format
Display a single integer which is the count of occurrences of '1' in the binary representations of all numbers from 1 to ( N ).

Constraints
0 < N<= 10^7

Sample Testcase 0
Testcase Input
4
Testcase Output
5
Explanation
for (1) => (0001), set bits = 1


for (2) => (0010), set bits = 1


for (3) => (0011), set bits = 2


for (4) => (0100), set bits = 1


Total set bits = 5


Therefore, for N = 4, result is 5

Sample Testcase 1
Testcase Input
5
Testcase Output
7
Explanation
Let input N = 5 then we have to count total set bits in digit 1 to 5,

for (1) => (0001), set bits = 1


for (2) => (0010), set bits = 1


for (3) => (0011), set bits = 2


for (4) => (0100), set bits = 1


for (5) => (0101), set bits = 2


Total set bits = 7


Therefore, for N = 5, result is 7
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=0
for i in range(1,n+1):
  k=bin(i)[2:]
  s+=k.count('1')
print(s)