'''
Problem Statement
We are given a string s consisting of only lowercase letters of english, and a character ch.

Your task is to reverse a portion of a string from the last occurrence of a given character ch to the end of the string.

Input Format
First line contains a string s and character ch.

Output Format
Print the transformed string.

Constraints
1<=|s.length|<=10^5

Sample Testcase 0
Testcase Input
abc c
Testcase Output
abc
Explanation
Last occurrence of c is the last character of the string, so reversing it won’t change the string.
Sample Testcase 1
Testcase Input
abxcced c
Testcase Output
abxcdec
Explanation
The last index of 'c' occurring is:4. Reversing the string from 4th index to last: "ced" to "dec". 
The final string therefore is: "abxcdec".
'''
a,b=input().split()
a=a.strip()
b=b.strip()
if b not in a:
  print(a)
else:
  k=a.rindex(b)
  c=a[k:]
  #print(c)
  print(a[:k]+c[::-1])