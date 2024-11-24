'''
Problem Statement
In this coding scenario, you have two arrays of boxes, word1 and word2. The task is to determine if these boxes, when stacked in the same order, create identical structures.

In other words, you should check if the elements in the two arrays, when concatenated in their respective orders, form the same string. If they do, the function should return true, indicating that the structures match; otherwise, it returns false, signifying a difference between the arrays.

Input Format
In the first line, you are given a single integer representing the the length of first array.
In the second line, you are given the elements of the first array (first box).
In the third line, you are given a single integer representing the the length of second array.
In the fourth line, you are given the elements of the second array (second box).
Output Format
A boolean value, true or false is returned.

Constraints
1 <= word1.length, word2.length <= 106
1 <= word1[i].length, word2[i].length <= 106
word1[i]and word2[i] consist of only lowercase letters.
Sample Testcase 0
Testcase Input
2
acd f
2
ac df
Testcase Output
true
Explanation
word1 when concatenated represents the string: "acdf" while word2 when concatenated represents: "acdf".


Therefore, as both the strings are same we return true. 

Sample Testcase 1
Testcase Input
3
ac e d
3
ac d e
Testcase Output
false
Explanation
word1 when concatenated represents: "aced" while word2 when concatenated represents: "acde".


As, "aced" != "acde" we return false
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=input().split()
c=int(input())
d=input().split()
b=''.join(b)
d=''.join(d)
if b==d:
  print("true")
else:
  print("false")