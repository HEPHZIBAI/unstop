'''
In the enchanted kingdom of puzzles and riddles, Princess Elara has entrusted her loyal companion, Prince Liam, with a magical challenge. Legend has it that within the kingdom exists a mystical set of numbers known as "Enchanted Numbers." These special numbers possess a unique property – they can be transformed using a secret formula.

Prince Liam's mission is to craft an algorithm that can distinguish these Enchanted Numbers from the ordinary ones. The magical process begins with any positive integer. Following a specific incantation, the number is replaced repeatedly with the sum of the squares of its digits. This enchanting ritual continues until the number either transforms into the revered number 1, becoming an Enchanted Number, or falls into a mysterious cycle, excluding the crave 1.

With the princess's trust in his abilities and the support of his loyal advisors (that's you!). Your invaluable guidance and wisdom are the beacon that illuminates his path, helping him unravel the secrets of these Enchanted Numbers. Together, you and Prince Liam venture into the realm of numbers and magic, where friendship and teamwork are the keys to unlocking the kingdom's most mysterious numerical secrets.

Input Format
The first line contains a positive integer n, representing the number to be checked as an Enchanted Number.

Output Format
Prince Liam needs to return 1 if it’s Enchanted Number and 0 if its not  an Enchanted Number.

Constraints
1 <= n <= 2^31 - 1

Sample Testcase 0
Testcase Input
18
Testcase Output
0
Explanation
18 is not a happy number because the process goes as follows: 1^2 + 8^2 = 65, 6^2 + 5^2 = 61, 6^2 + 1^2 = 37, 3^2 + 7^2 = 58, 5^2 + 8^2 = 89, 8^2 + 9^2 = 145, 1^2 + 4^2 + 5^2 = 42, 4^2 + 2^2 = 20, 2^2 + 0^2 = 4, 4^2 = 16, 1^2 + 6^2 = 37 (the cycle repeats).

Sample Testcase 1
Testcase Input
7
Testcase Output
1
Explanation
7 is a happy number because the process goes as follows: 7^2 = 49, 4^2 + 9^2 = 97, 9^2 + 7^2 = 130, 1^2 + 3^2 + 0^2 = 10, 1^2 + 0^2 = 1.
'''

n=int(input())

while(n>6):
  l=n
  s=0
  while l>0:
    r=l%10
    s+=r*r
    l//=10
  
  n=s

if n==1:
  print(1)
else:
  print(0)