/*
Problem Statement
One day, Mary wanted to give a present to her friend. She decided on a beautiful bouquet of flowers and began collecting them. She needed precisely 2 types of flowers, and the total number of flowers required was 't'. To gather these, she started picking from her garden, which contained 'N' types of flowers. Each type was arranged in a queue in non-decreasing order, such as 1, 3, 6, 15, and so forth.

Now, she seeks your help in determining the indexes of the flowers she should collect.

Note: For every case, there will always be a pair of flowers that sums up to 't'.

Input Format
The first line contains integers N and t where, N is the total types of flowers and t is the total number of flowers needed.

The second line contains n integers a1,a2,…,an — elements of the a array.

Output Format
Print the indexes of the two flowers that sum up to 't'. The first index should be smaller than the second index. Both indexes should be zero-based.

Constraints
2 <= N <= 10^4
1 <= a[i] <= 10^3
2 <= t <= 2*10^3
here is exactly one solution exist.
Sample Testcase 0
Testcase Input
7 5
1 2 2 4 5 7 10
Testcase Output
0 3
Explanation
The sum of flowers at index 0 and index 3 is 1 + 4 = 5, which matches the required total number of flowers needed..

Sample Testcase 1
Testcase Input
5 2
1 1 2 3 4
Testcase Output
0 1
Explanation
The sum of flowers at index 0 and index 1 is 1 + 1 = 2, which matches the required total number of flowers needed..
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    long int n,t;
    scanf("%ld%ld",&n,&t);
    long int a[n];

    for(int i=0;i<n;i++)
        scanf("%ld",&a[i]);

    for(int i=0;i<n;i++)
    {
        int m=0;
        for(int j=i+1;j<n;j++)
        {
            if(a[i]+a[j]==t)
            {
                printf("%d %d",i,j);
                m=1;
                break;
            }
        }
        if(m==1)
            break;
    }
    return 0;
}