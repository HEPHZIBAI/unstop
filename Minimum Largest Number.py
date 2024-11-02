'''Problem Statement
Given an array of integers arr[] of size N, find the two smallest integers in the array and form the largest possible number using them. Output this largest number

Input Format
The first line contains an integer, where N denotes the number of elements in the array in the array.

The second line contains N space-separated integers.

Output Format
Print the largest number that can be formed.

Constraints
1 ≤ N ≤ 10^2

0 ≤ arr[i] ≤9

Sample Testcase 0
Testcase Input
7
1 2 3 4 5 6 7
Testcase Output
21
Explanation
The two minimum numbers out of the given array are 1 and 2. If we try to make the largest number possible using these two numbers, we get 21.
Sample Testcase 1
Testcase Input
4
7 8 9 6
Testcase Output
76
Explanation
The two minimum numbers out of the given array are 6 and 7. If we try to make the largest number possible using these two numbers, we get 76.'''



n=int(input())

a=list(map(int,input().split()))

l1=min(a)
a.remove(l1)
l2=min(a)

h1=(l1*10)+l2
h2=(l2*10)+l1
print(h1 if h1>h2 else h2 )