'''
Ram and Shyam have devised a new encoding scheme called "Reverse Mirror Encoding." In this system:

For letters 'a' to 'n', the code is their reverse position in the first half of the alphabet.

Example: 'a' → n, 'b' → m, ..., 'n' →a.
For letters 'o' to 'z', the code is their reverse position in the second half of the alphabet followed by a #.

Example: 'o#' → z, 'p#' → y, ..., y# → p, 'z#' → o.
Given a coded message S, determine the original decoded message Ram sent to Shyam.

Input Format
The first and only line of input contains a single string S, representing the encoded message.

 
Output Format
Print a single string, representing the decoded message.

Constraints
2 <= |S| <= 10^3

Sample Testcase 0
Testcase Input
u#jlg
Testcase Output
tech
Explanation
'u#' → 't'.
'j' → 'e'.
'l' → 'c'.
'g' → 'h'.
Decoded message: "tech".

Sample Testcase 1
Testcase Input
mjt#av#u#z#y#y#nmcj
Testcase Output
beunstoppable
Explanation
'm' → 'b'.
'j' → 'e'.
't#' → 'u'.
'a' → 'n'.
'v#' → 's'.
'u#' → 't'.
'z#' → 'o'.
'y#' → 'p'.
'y#' → 'p'.
'n' → 'a'.
'm' → 'b'.
'c' → 'l'.
'j' → 'e'.
Decoded message: "beunstoppable".
'''

def decode_message(encoded):
    a='abcdefghijklmn'
    b='opqrstuvwxyz'
    ans=''

    for i in range(len(encoded)):
        if encoded[i]=='#':
            continue
        else:
            if encoded[i] in a:
                k=a.index(encoded[i])+1
                k*=-1
                ans+=a[k]
            else:
                k=b.index(encoded[i])+1
                k*=-1
                ans+=b[k]
    return ans

if __name__ == "__main__":
    encoded = input()
    decoded = decode_message(encoded)
    print(decoded)