'''
Problem Statement
Reena has a basket containing an array of 2N fruits.

She needs to pair these fruits into N pairs, (a1, b1) , (a2, b2),.....,(an, bn), such that the sum of the minimum values in each pair, min(ai, bi) for all i is maximized.
Your task is to calculate and print this maximum possible sum.

Input Format
The first line contains a single even integer representing the number of fruits, 2N.

The second line contains 2N space-separated integers representing the fruits.

Output Format
Print a single integer, which is the maximum sum.

Constraints
1 <= N <= 10^5

length == 2 * N

-10^4 <= nums[i] <= 10^4

Sample Testcase 0
Testcase Input
 6
5 3 2 1 6 3
Testcase Output
9
Explanation
As to get maximum sum in this case our answer would be
Min(1,2) + min(3,3) + min(5,6) = 9
Sample Testcase 1
Testcase Input
8
5 7 6 2 9 1 1 4
Testcase Output
15
Explanation
As to get maximum sum in this case our answer would be
Min(1,1) + min(2,4) + min(5,6) + min(7,9) = 15
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=list(map(int,input().split()))
a.sort()
x=a[:len(a)//2]
y=a[len(a)//2:]
#print(x,y)
s=0
for i in range(0,len(a),2):
  s+=a[i]
print( s)