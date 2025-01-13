'''
Sid is reading a paragraph of a story and notices N different sentences. He's curious to know which sentence is the longest.

Help Sid find the length of the longest sentence in the story. Sentences are separated by  a comma(,),no other symbols are used except comma.

Input Format
The first line of input contains a string where sentences are separated by commas ( ,) .

Output Format
Display a single integer, that denotes the length of the longest sentence.

Constraints
 1<=N<=20

Sample Testcase 0
Testcase Input
Ram is a good boy. He drinks a lot of water. He stays in Shimla.
Testcase Output
6
Explanation
Here are three sentences:


1. "Ram is a good boy" (length = 5 words)
2. "He drinks a lot of water" (length = 6 words)
3. "He stays in Shimla" (length = 4 words)


The second sentence is the longest, with a length of 6 words, so we print 6.

Sample Testcase 1
Testcase Input
Early to bed and early to rise makes a man healthy, wealthy and wise.
Testcase Output
11
Explanation
Here are two sentences:


1. "Early to bed and early to rise makes a man healthy" (length = 11 words)
2. "wealthy and wise" (length = 3 words)


The first sentence is the longest, with a length of 11 words, so we print 11.
'''

def find_longest_sentence_length(s):
    s=s.split('.')
    l=0
    for i in s:
        i=i.split(',')
        for j in i:
            j=j.split()
            if len(j)>l:
                l=len(j)
    return l


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    # Call user logic function and print the output
    result = find_longest_sentence_length(s)
    print(result)

if __name__ == "__main__":
    main()