'''
Problem Statement
You are given a row of boxes. Each box can be either "a" or "b".

To check if it's an 'ab' pattern, you need to make sure that all the "a" boxes, if they exist, come before any "b" boxes, if they exist.

If this order is maintained, it's an ab pattern; otherwise, it's not. Display "YES" if it is maintained else "NO". 

Input Format
The first and only line of input contains a string S, representing the row of boxes. 

Output Format
Print "YES" if the sequence follows the "ab" pattern; otherwise, print "NO."

Constraints
1<= S.length <=106

Sample Testcase 0
Testcase Input
aaaaab
Testcase Output
YES
Explanation
In the given sequence of boxes:


All the boxes with 'a's are occuring before boxes with 'b's. 


So we print "YES".

Sample Testcase 1
Testcase Input
aaba
Testcase Output
NO
Explanation
In the given sequence of boxes:


The boxes with 'a' at index 3 is occuring after the box with 'b' so it doesn't follow the ab pattern.


So we print "NO".
'''



# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input().strip()

i=0
k=""
while(i<len(a)):
  if i<len(a) and a[i]=='a':
    k+='a'
    while(i<len(a) and a[i]=='a'):
      i+=1
  if i<len(a) and a[i]=='b':
    k+='b'
    while(i<len(a) and a[i]=='b'):
      i+=1

if len(k)%2!=0:
  if k=='a' or k=='b':
    print("YES")
  else:
    print("NO")
else:
  for i in range(0,len(k),2):
    if k[i:i+2]!='ab':
      print("NO")
    else:
      print("YES")

#print(k)