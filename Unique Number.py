'''
You are given an integer N with a value in the range [−10^18,10^18]. Your task is to find an integer A such that 0≤A<998244353−1  and the following condition holds:

(N−A) is divisible by 998244353.
It can be proved that such an integer is unique.

Input Format
You are given an integer N.

Output Format
Find the integer A satisfying the condition.

Constraints
-10^18 <= N <= 10^18

Sample Testcase 0
Testcase Input
998244354
Testcase Output
1
Explanation
998244354−1=998244353 is a multiple of 998244353, so the condition is satisfied.

Sample Testcase 1
Testcase Input
-9982443534
Testcase Output
998244349
Explanation
−9982443534−998244349=−10980687883 is a multiple of 998244353, so the condition is satisfied.
'''


n=int(input())

k=n%998244353
print(k)