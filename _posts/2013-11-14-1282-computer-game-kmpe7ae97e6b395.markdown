---
author: lufo
comments: true
date: 2013-11-14 15:42:24+00:00
layout: post
slug: 1282-computer-game-kmp%e7%ae%97%e6%b3%95
title: 1282. Computer Game KMP算法
wordpress_id: 111
tags:
- 编程
---

<blockquote>

> 
> Description
> 
> 

> 
> 

Brian is an enthusiast of computer games, especially those that simulate virtual reality. Now he is in front of the Star Gate. In order to open the gate he must break the protection as quickly as he can. Breaking the protection means to match a given code (a sequence of numbers) against the gate protection (a very long sequence of numbers). The starting position of the first occurrence of the code within the sequence opens the gate. Can you help him?

The code is a sequence of at most **60000** integer numbers between **0** and **255**. The gate protection contains integer numbers between **0**and **255**. Your program must find the first match if there is one, or report the absence of a match.


> 
> 

> 
> Input
> 
> 

> 
> 

The text input file contains several data sets. Each data set has the following format:

l     the length of the code

l     the sequence of numbers representing the code

l     the number of integers in the gate protection

l     the sequence of numbers representing the gate protection** **

**code_dimension
****integer1 integer2 … integercode_dimension
****protection_dimension
****integer1 integer2 … integerprotection_dimension**

****White spaces may occur freely in the input.


> 
> 

> 
> Output
> 
> 

> 
> 

The results must be printed on the standard output. For each given data set, print the result on a separate line. The result is a number that represents the position (starting from zero) of the first occurrence of the code in the gate protection, or the message **no solution **if there is no match.


> 
> 

> 
> Sample Input
> 
> 

> 
>  Copy sample input to clipboard
> 
> 

> 
> 

>     
>     3
>     0 1 2
>     7
>     2 3 4 0 1 2 5
>     
>     2
>     1 4
>     6
>     4 1 4 1 4 4
>     
>     3
>     1 2 3
>     7
>     3 2 1 3 2 255 7
> 
> 

> 
> 

> 
> Sample Output
> 
> 

> 
> 

>     
>     3
>     1
>     no solution
> 
> 

> 
> </blockquote>


本质就是用KMP算法进行字符串匹配，对KMP不了解可参考[http://chaoswork.com/blog/2011/06/14/kmp%E7%AE%97%E6%B3%95%E5%B0%8F%E7%BB%93/](http://chaoswork.com/blog/2011/06/14/kmp%E7%AE%97%E6%B3%95%E5%B0%8F%E7%BB%93/)

代码如下：

[cpp]

#include <iostream>
#include <cstring>
using namespace std;

void SetNext(int n, int b[], int next[]) {
 next[0] = 0;
 int i = 0, k = 0;
 for (i = 1; i < n; i++) {
 k = next[i - 1];
 while (b[i] != b[k] && k > 0)
 k = next[k - 1];
 if (b[i] == b[k]) {
 next[i] = k + 1;
 } else
 next[i] = 0;
 }
}

int main() {
 int n, m;
 int next[60000];
 int i = 0, j = 0;
 while (cin >> n) {
 int a[n];
 for (i = 0; i < n; i++) {
 cin >> a[i];
 }
 cin >> m;
 int b[m];
 for (i = 0; i < m; i++) {
 cin >> b[i];
 }
 SetNext(n, a, next);
 i = 0, j = 0;
 while (true) {
 if (b[i] == a[j]) {
 if (j == n - 1) {
 cout << i - n + 1 << endl;
 break;
 }
 i++;
 j++;
 } else {
 if (j > 0)
 j = next[j - 1];
 else
 i++;
 }
 if (i == m) {
 cout << "no solution" << endl;
 break;
 }
 }
 }
 return 0;
}

[/cpp]
