'''
Problem Statement
Ronak, a young wizard with the power to identify palindromic words, was exploring an array of strgin A of length N filled with ancient strings. He decided to find the first palindromic string from the array using his abilities.

Note: strgin in array A consist of onyl lowercase English alphabets.

Input Format
The first line contains an integer N that will be passed,, representing the size of the array A.

The next line contains N strings separated by spaces for arrray A.

Output Format
Print the first palindromic string in the array. If there is no such string, return an empty string "".

Constraints
1 <= N <= 10^5


1 <= A[i]<= 10^2

Sample Testcase 0
Testcase Input
5
hello world level algorithm madam
Testcase Output
level
Explanation
The first palindromic word in the given list is "level" because it reads the same forward and backward.

Sample Testcase 1
Testcase Input
4
hello world python programming
Testcase Output
Explanation
There are no palindromic words in the given list, so the function returns an empty string ("").
'''

n=int(input())
a=input().strip()
if a=="":
    a=input().strip()

a=a.split()

for i in a:
    i=i.strip()
    if i==i[::-1]:
        print(i)
        break