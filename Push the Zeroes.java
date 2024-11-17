/*
Problem Statement
You are given an array, containing numbers and zeroes, you need to push all the zeroes to the end of the array. Notice that while pushing the zeroes the relative ordering between the non-zero elements should not change.

Given an array, push the zeroes and print the array.

Input Format
The first line of the input contains ‘n’ the number of elements in the array.

The following line contains n numbers, arr[i], the elements of the array.

Output Format
Print the array after pushing the zeroes.

Constraints
1<=n<=105

-100<=arr[i]<=100

Sample Testcase 0
Testcase Input
4
0 0 0 1
Testcase Output
1 0 0 0 
Explanation
Keeping the order of non zero elements the same and appending the zeroes in the end the resultant array is 1 0 0 0
Sample Testcase 1
Testcase Input
5
1 0 2 0 3
Testcase Output
1 2 3 0 0
Explanation
After appending the zeroes in the end the result array becomes 1 2 3 0 0
*/



import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        int b=0;
        for(int i=0;i<n;i++)
        {
            int c=sc.nextInt();
            if(c != 0)
            {
                a[b]=c;
                b++;
            }
        }
        
        for(int i=0;i<n;i++)
        {
            System.out.print(a[i]);
            System.out.print(" ");
        }
    }
}