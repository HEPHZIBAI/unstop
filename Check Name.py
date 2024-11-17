'''

Problem Statement
Alex and Bob want to find out the common characters between N strings of names. Help Alex and Bob find it.

Print the common letters in lexicographical order.

Input Format
The first line contains a single digit N (no of strings).
The next N lines contain the strings.
Output Format
You have to print all of the common characters that strictly appear in every single string in lexicographical order.

Note: Each common character should be displayed in square brackets '[]'.

Constraints
1<=n<=100
1<=n[i].size()<=50000
Sample Testcase 0
Testcase Input
2
Bella
alex
Testcase Output
[a][e][l]
Explanation
Bella and Alex have a, l and e in common.

Sample Testcase 1
Testcase Input
3
abcd
cdef
mdec
Testcase Output
[c][d]
Explanation
In all three strings, the letters c and d are common. So, in lexicographical order, the output is: [c][d]


'''

n=int(input())
a=[]
ans=[]
for i in range(n):
  a.append(input().strip())

sss=list(set(a[0]))

for i in sss:
  s=0
  h=len(a[0])
  for j in a:
    if i in j:
      s+=1
      if h>j.count(i):
        h=j.count(i)

  if s==len(a):
    for k in range(h):
      ans.append(i)

ans.sort()
for i in ans:
  print("["+i+"]",end="")
#print(ans)