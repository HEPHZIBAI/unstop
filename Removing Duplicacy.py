'''
Given a string, you can perform the below-mentioned operation till the duplicacy of the string is not removed. A string is said to contain duplicacy if any two adjacent characters are the same.

A duplicate removal consists of choosing two adjacent and equal letters and removing them.

You can repeatedly make duplicate removals on the given string until you no longer can.

Print the string after removing the duplicacyof the string.

 

Input Format
The first line of the input consists of s, the string you have to eliminate its duplicacy.

 

Output Format
Print the given string after removing the duplicacy of the string.

Constraints
1<=n<=105,n refers to the size of the given string.

 

Sample Testcase 0
Testcase Input
ccbbadef
Testcase Output
adef
Explanation
In ccbbadef, the duplicates are cc. After removing them, the string becomes bbadef; similarly, we can remove bb and string becomesadef.

Sample Testcase 1
Testcase Input
abbacad
Testcase Output
cad
Explanation
In abbacad, we can remove bb; after removing the string becomes aacad, now we can remove aa, so the string becomes cad.

'''

a=input()
b=""
for i in a:
  if len(b)==0:
    b+=i
  elif b[-1]==i:
    b=b[:len(b)-1]
  else:
    b+=i
print(b)