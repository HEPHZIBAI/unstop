'''
Problem Statement
Ram had an array of integers .He wants to know whether he can make an arithmetic progression using this sequence or not?

Note: You have to include all elements .

Numbers present in the array are unsorted.

Help Ram in finding whether he can make an arithmetic progression using sequence or not?

Return true if he can make a sequence using this else false.

 

Input Format
First line contains the size of the array ,i.e. n.

Second line n space-separated integers .

Output Format
True or false.

Constraints
2<=arr.size()<=200

1<=arr[i]<=10000

 

Sample Testcase 0
Testcase Input
5
24 72 48 0 96
Testcase Output
true
Explanation
0 24 48 72 96 forms an arithmetic sequence with common difference 24.
Sample Testcase 1
Testcase Input
7
89 88 32 34 93 3 23
Testcase Output
false

Explanation
3 23 32 34 88 89 93 doesn’t form an arithmetic sequence .
'''


n=int(input())
a=list(map(int,input().split()))
a.sort()
m=0
x=a[1]-a[0]

for i in range(n-1):
  if a[i+1]-a[i]!=x:
    print("false")
    m=1
    break

if m==0:
  print("true")