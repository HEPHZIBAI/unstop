/*
Problem Statement
There is a Chocolate shop, which initially had 0 chocolates.

There are two types of queries-

The owner adds any chocolate of quantity X.
Some customer wants to buy X no of chocolates of Y type.
Input Format
The first line contains Q, the no of queries to be made.

The following Q lines will contain the queries of type 1 or type 2.

Q

event 1

event 2

⋮

event Q

Output Format
When a customer comes to buy some X chocolate of Y type, output the X number if the seller has a minimum of X number of chocolate of Y type.

Else output the max number he can sell of that type of chocolate to the customer.

In both cases, decrease the quantity available to the seller.

Constraints
2 ≤ Q ≤ 5×10^5

Sample Testcase 0
Testcase Input
2
1 Bubaloo 5
2 Bubaloo 2
Testcase Output
2
Explanation
The first query is, adding Bubaloo chocolate of quantity 5.


The second query is someone is asking for Bubaloo chocolate of quantity 2, as he has that number of chocolates so he returns 2.

Sample Testcase 1
Testcase Input
4
1 Tofee 4
1 Chupachoop 2
2 Tofee 3
2 Tofee 2
Testcase Output
3
1
Explanation
The first query is adding Tofee of quantity 4.


The Second query is adding ChupaChoop of quantity 2.


The third query is selling Tofee of quantity 3. As he has that number in stock, he returns 3.


The fourth query is selling Tofee of quantity 2. As he does not have that number in stock, he returns the number of stock he has, which is 1.*/


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main {

    public static void main(String[] args) 
    {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for(int i=0;i<n;i++)
        {
            String[] a=sc.nextLine().split(" ");
            if(Integer.parseInt(a[0])==1)
            {
                if(map.containsKey(a[1]))
                {
                    map.put(a[1],map.get(a[1])+Integer.parseInt(a[2]));
                }
                else
                    map.put(a[1],Integer.parseInt(a[2]));
            }
            else
            {
                if(map.containsKey(a[1]))
                {
                    int con=map.get(a[1]);
                    if(con>=Integer.parseInt(a[2]))
                    {
                        System.out.println(a[2]);
                        map.put(a[1],map.get(a[1])-Integer.parseInt(a[2]));
                    }
                    else
                    {
                        System.out.println(con);
                        map.put(a[1],0);
                    }
                }
                else
                {
                    System.out.println(0);
                }
            }
        }
        //System.out.println(map);
    }
}