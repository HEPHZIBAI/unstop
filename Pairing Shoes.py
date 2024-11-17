'''
Problem Statement
In a shoe factory, left and right shoes are produced separately, each with an integral ID according to its design and size. After manufacturing, the shoes are sent to Bob, who pairs left and right shoes with matching IDs. Each shoe can only be paired once, and the manager wants to know the IDs of all matching pairs in sorted order before final packaging.

Input Format
The first line of the input contains two integers, n and m – the number of left and right shoes, respectively.

The second line contains n space-separated integers a1, a2, ..., an – the IDs of all the left shoes

The third line contains m space-separated integers b1, b2, ..., bm – the IDs of all the right shoes.

Output Format
In the first line, print p – the number of pairs that will be ready

In the next line, print p space-separated integers – the IDs of all the pairs that will be ready in sorted order.

Constraints
1 <= n, m <= 10^4

0 <= ai, bi <= 10^4

Sample Testcase 0
Testcase Input
3 5
4 9 5
9 4 9 8 4
Testcase Output
2
4 9
Explanation
We can observe that for the left shoes 4 and 9, there exists a right shoe with the same ID.


But the left shoe 5 will be left unpaired.


Also, the remaining right shoes with IDs 9, 8, 4 will be left unpaired.

Sample Testcase 1
Testcase Input
4 2
1 2 2 1
2 2
Testcase Output
2
2 2
Explanation
For both of the right shoes with ID 2, there exists a left shoe with the same ID. So, two pairs can be made, both will have ID 2.


There is no right shoe with ID 1, so the two left shoes with ID 1 will remain unpaired.
'''


n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]

if n<m:
  for i in a:
    if i not in c and i in a and i in b:
      x=a.count(i)
      y=b.count(i)
      for j in range(min(x,y)):
        c.append(i)
else:
  for i in b:
    if i not in c and i in a and i in b:
      x=a.count(i)
      y=b.count(i)
      for j in range(min(x,y)):
        c.append(i)

c.sort()
print(len(c))
for i in c:
  print(i,end=" ")
