'''
Problem Statement
Rose is working with binary numbers and has been given two strings, str1 and str2. She wants to determine if str2 can be rearranged to match str1. If this is possible, print the length of the string in its binary representation. If not, print 0.

Note: Both strings are guaranteed to have the same length.

Input Format
The first line contains the string str1.

The second line contains the string str2.

Output Format
Print the resultant binary form.

Constraints
1 <= str1.length <= 1e5

1 <= str2.length <= 1e5

str1 and str2 contain lowercase English alphabets.

Sample Testcase 0
Testcase Input
abc
abd
Testcase Output
0
Explanation
The strings can not be the same after rearrangement. So, 0 is printed.
Sample Testcase 1
Testcase Input
fg
gf
Testcase Output
10
Explanation
The str2 can be rearranged as str1. So, the size of the given string i.e., 2, is printed in binary
'''


a=input().strip()
b=input().strip()
m=0

for i in set(a):
  if a.count(i)!=b.count(i):
    m=1
    break

for i in set(b):
  if a.count(i)!=b.count(i):
    m=1
    break

if m==0:
  print(bin(len(a))[2:])
else:
  print(0)