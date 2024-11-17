'''
Problem Statement
Marco likes words a lot. But he likes them in lowercase only.

He got a book from his friend where words are written in upper and lowercase characters.

Help Marco to convert all words in lowercase.

Input Format
The first line contains the string word.

Output Format
The first line contains the transformed string in lower case.

Constraints
1 <= word.length <= 10^5

Word consists of lower case and upper case alphabets only.

Sample Testcase 0
Testcase Input
here
Testcase Output
here
Explanation
There is no upper-case character present in the input given. Hence, the output remains the same.
Sample Testcase 1
Testcase Input
Hello
Testcase Output
hello		
Explanation
‘H’ in ‘Hello’ is converted to ‘h’ in the input given.
'''
a=input().strip()
print(a.lower())