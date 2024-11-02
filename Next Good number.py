'''
Problem Statement
A good number is a number that contains all odd digits in it like 1113 is a good number because all the digits are odd.

You are given a number x you need to tell the next largest number which is greater than x and a good number.

Input Format
The first line will contain T, the number of test cases. The description of T test cases follows.
Each line contains an integer x.
Output Format
For each test case, you need to print the next greatest good number.
Constraints
1<=T<=10^6
1<=x<=10^6
Sample Testcase 0
Testcase Input
1
11
Testcase Output
13
Explanation
13 is the next greatest number of 11 which contains all odd digits.
Sample Testcase 1
Testcase Input
2
26
16
Testcase Output
31
17
Explanation
31 is the next greatest number of 26 which contains all odd digits. 17 is the next greatest number of 16 which contains all odd digits'''


n=int(input())
for i in range(n):
  a=input().strip()
  a=str(int(a)+1)
  m=1
  while(m==1):
    m=0
    for j in a:
      if j in "24680":
        m=1
        break
    if m==1:
      a=str(int(a)+1)
  print(a)