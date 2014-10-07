---
author: lufo
comments: true
date: 2013-11-01 02:29:22+00:00
layout: post
slug: 1028-hanoi-tower-sequence
title: 1028. Hanoi Tower Sequence
wordpress_id: 86
tags:
- 编程
---

<blockquote>

> 
> # Constraints
> 
> 
Time Limit: 1 secs, Memory Limit: 32 MB

> 
> # Description
> 
> 
Hanoi Tower is a famous game invented by the French mathematician Edourard Lucas in 1883. We are given a tower of n disks, initially stacked in decreasing size on one of three pegs. The objective is to transfer the entire tower to one of the other pegs, moving only one disk at a time and never moving a larger one onto a smaller.

The best way to tackle this problem is well known: We first transfer the n-1 smallest to a different peg (by recursion), then move the largest, and finally transfer the n-1 smallest back onto the largest. For example, Fig 1 shows the steps of moving 3 disks from peg 1 to peg 3.
![](http://soj.me/UserFiles/c12/ximage001.gif.pagespeed.ic.TIJBzWOoZ2.png)

Now we can get a sequence which consists of the red numbers of Fig 1: 1, 2, 1, 3, 1, 2, 1. The ith element of the sequence means the label of the disk that is moved in the ith step. When n = 4, we get a longer sequence: 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1. Obviously, the larger n is, the longer this sequence will be.
Given an integer p, your task is to find out the pth element of this sequence.

> 
> # Input
> 
> 
The first line of the input file is **T**, the number of test cases.
Each test case contains one integer **p** (1<=p<10^100).

> 
> # Output
> 
> 
Output the pth element of the sequence in a single line. See the sample for the output format.
Print a blank line between the test cases.

> 
> # Sample Input
> 
> 

>     
>     4
>     1
>     4
>     100
>     100000000000000
> 
> 

> 
> # Sample Output
> 
> 

>     
>     Case 1: 1
>     
>     Case 2: 3
>     
>     Case 3: 3
>     
>     Case 4: 15
> 
> 

> 
> # Problem Source
> 
> 
ZSUACM Team Member</blockquote>


仔细观察，发现序列为1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1......即**n第一次出现的位置为2^n-1**，根据这一特点，若前p项的最大值max是第p_max项，则第p项的值为第p-p_max项的值，于是想出了第一种递归方法：

[cpp]

#include<iostream>
#include<cmath>
using namespace ::std;

int find(double p) {
 int i = 0;
 while (true) {
 if (pow(2.0, i) * 2 > p) {
 if (p - pow(2.0, i) == 0) {
 return i + 1;
 } else {
 return find(p - pow(2.0, i));
 }
 } else
 i++;
 }
}

int main() {
 int t = 0, i = 0;
 double p = 0;
 cin >> t;
 for (i = 0; i < t; i++) {
 cin >> p;
 cout << "Case " << i + 1 << ": " << find(p) << endl;
 if (i < t - 1)
 cout << endl;
 }
 return 0;
}

[/cpp]

毕竟too young too simple，一直WA却摸不到头脑，看了半天才发现尼玛p取值能达到10^100，这不坑爹嘛，看来只能用字符串储存p了，于是想到第二个方法。

第一种方法其实就是不断让p等于p减去小于p的2^i的最大值，直到p本身等于2^i，可证明最后得到的p能被2整除的次数和最初的p能被2整除的次数相等，所以**第p项的值为p能被2整除的次数**。程序如下：

[cpp]

#include<iostream>
#include<cstring>
using namespace ::std;

void div(int *p, int &low, int high) {
 int i = 0;
 for (i = low; i <= high; i++) {
 if (p[i] % 2 == 0)
 p[i] = p[i] / 2;
 else {
 p[i] = (p[i] - 1) / 2;
 p[i + 1] += 10;
 }
 }
 if (p[low] == 0)
 low++;
}

int main() {
 int t = 0, i = 0, j = 0;
 int p[101];
 char s[102];
 cin >> t;
 for (i = 0; i < t; i++) {
 cin >> s;
 int length = strlen(s);
 int low = 0;
 int n = 1;
 for (j = 0; j < length; j++) {
 p[j] = s[j] - '0';
 }
 while (p[length - 1] % 2 == 0) {
 div(p, low, length - 1);
 n++;
 }
 cout << "Case " << i + 1 << ": " << n << endl;
 if (i < t - 1)
 cout << endl;
 }
 return 0;
}

[/cpp]
