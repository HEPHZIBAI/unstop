/*
Problem Statement
Given `A` `B` `C` integer

Perform And, OR, XOR, shift Operation of given two numbers.

The first digit Should be the left Shift, and the Second digit should be the right shift

Input Format
First line contains `A` Integer 

Second line contains `B` Integer

Third line contains `C` Integer represent shifted by this number

Output Format
Perform And, OR, XOR, shift Operation of given two numbers.

Constraints
0 <= A,B,C <= 100

Sample Testcase 0
Testcase Input
1
2
2
Testcase Output
AND Result: 0
OR Result: 3
XOR Result: 3
Left Shift Result: 4
Right Shift Result: 0
Explanation
1 And 2 get 0


1 or 2 get 3


1 xor 2 get 3


Left shift of 1 get 4


Right shift of 2 get 0

Sample Testcase 1
Testcase Input
2
2
2
Testcase Output
AND Result: 2
OR Result: 2
XOR Result: 0
Left Shift Result: 8
Right Shift Result: 0
Explanation
2 And 2 get 2


2 or 2 get 2


2 xor 2 get 0


Left shift of 2 get 8


Right shift of 2 get 0*/



import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main {

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        System.out.println("AND Result: "+(a&b));
        System.out.println("OR Result: "+(a|b));
        System.out.println("XOR Result: "+(a^b));
        System.out.println("Left Shift Result: "+(a<<c));
        System.out.println("Right Shift Result: "+(b>>c));
    }
}