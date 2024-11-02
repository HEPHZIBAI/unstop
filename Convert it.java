/*
Problem Statement
Given an array of integer, an astrologer has determined that it is not lucky and needs to be changed.

The suggested modification involves increasing the value at each index by the maximum value encountered up to that index. Your task is to print the modified array.

Input Format
The first line contains a single integer N, representing the size of the array.

The second line contains N space-separated integers, representing the elements of the array.

Output Format
Print the modified array after applying the suggested changes.

Constraints
1 <= N <= 100

0 <= A[i] <= 10^4

Sample Testcase 0
Testcase Input
1
12
Testcase Output
24
Explanation
Maximum value encountered till each index


Index      value
1                 12


Changed array: 12+12 


Output: 24

Sample Testcase 1
Testcase Input
3 
1 2 3
Testcase Output
2 4 6
Explanation
Initial Array: [1 2 3]
Maximum value encountered till each index


Index      value
1                 1
2                 2
3                 3


Changed array: 1+1, 2+2, 3+3
Output: [2 4 6]*/


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main 
{
    public static void main(String[] args) 
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        //int[n] a=new int[n];
        int l=0;
        for(int i=0;i<n;i++)
        {
            int a=sc.nextInt();
            if(a>=l)
            {
                l=a;
            }
            System.out.print(a+l+" ");
        }
    }
}