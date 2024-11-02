/*
Problem Statement
Alice challenged Bob to write the same word as his on a typewriter. Both are kids and are making some mistakes in typing and are making use of the ‘#’ key on a typewriter to delete the last character printed on it.

An empty text remains empty even after backspaces. 

Input Format
The first line contains a string typed by Bob.

The second line contains a string typed by Alice.

Output Format
The first line contains ‘YES’ if Alice is able to print the exact words as Bob , otherwise ‘NO’.

Constraints
1 <= Bob.length

Alice.length <= 100000

Bob and Alice only contain lowercase letters and '#' characters.

Sample Testcase 0
Testcase Input
ab#c
ad#c
Testcase Output
YES
Explanation
Here ,
The actual typed string by Bob : ‘ac’
The actual typed string by Alice : ‘ac’
Hence , they matched.
Sample Testcase 1
Testcase Input
a#c
b
Testcase Output
NO
Explanation
Here ,
The actual typed string by Bob : ‘c’
The actual typed string by Alice : ‘b’
Hence , they do not matched.
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    char a[100000],b[100000];
    char x[100000],y[100000];

    scanf("%s\n%s",a,b);
    int m=0;

    for(int i=0;i<strlen(a);i++)
    {
        if(a[i]!='#')
        {
            x[m]=a[i];
            m+=1;
        }
        else if(a[i]=='#')
        {
            m-=1;
        }
        if(m<0)
            m=0;
    
    }
    x[m]='\0';
    int n=0;
    for(int i=0;i<strlen(b);i++)
    {
        if(b[i]!='#')
        {
            y[n]=b[i];
            n+=1;
        }
        else if(b[i]=='#')
        {
            n-=1;
        }
        if(n<0)
            n=0;
    }
    y[n]='\0';
    if(m==n)
    {
        int f=0;
        for(int i=0;i<m;i++)
        {
            if(x[i]!=y[i])
            {
                f=1;
                break;
            }
        }
        if(f==0)
            printf("YES");
        else
            printf("NO");
    }
    else
        printf("NO");
    //printf("%s\n%s",x,y);
    /*#a#a#a
    a#a#a#*/
    return 0;
}