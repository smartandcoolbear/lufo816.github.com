---
author: lufo
comments: true
date: 2013-11-03 08:09:16+00:00
layout: post
slug: 1002-anti-prime-sequences-%e5%9b%9e%e6%ba%af%e6%b3%95%e5%88%9d%e6%8e%a2
title: 1002. Anti-prime Sequences 回溯法初探
wordpress_id: 88
categories:
- 编程
---

<blockquote>

> 
> # Constraints
> 
> 
Time Limit: 3 secs, Memory Limit: 32 MB

> 
> # Description
> 
> 


Given a sequence of consecutive integers n,n+1,n+2,...,m, an anti-prime sequence is a rearrangement of these integers so that each adjacent pair of integers sums to a composite (non-prime) number. For example, if n = 1 and m = 10, one such anti-prime sequence is 1,3,5,4,2,6,9,7,8,10. This is also the lexicographically first such sequence. We can extend the definition by defining a degree danti-prime sequence as one where all consecutive subsequences of length 2,3,...,d sum to a composite number. The sequence above is a degree 2 anti-prime sequence, but not a degree 3, since the subsequence 5, 4, 2 sums to 11. The lexicographically .rst degree 3 anti-prime sequence for these numbers is 1,3,5,4,6,2,10,8,7,9.



> 
> # Input
> 
> 


Input will consist of multiple input sets. Each set will consist of three integers, n, m, and d on a single line. The values of n, m and d will satisfy 1 <= n < m <= 1000, and 2 <= d <= 10. The line 0 0 0 will indicate end of input and should not be processed.



> 
> # Output
> 
> 


For each input set, output a single line consisting of a comma-separated list of integers forming a degree danti-prime sequence (do not insert any spaces and do not split the output over multiple lines). In the case where more than one anti-prime sequence exists, print the lexicographically first one (i.e., output the one with the lowest first value; in case of a tie, the lowest second value, etc.). In the case where no anti-prime sequence exists, output No anti-prime sequence exists.



> 
> # Sample Input
> 
> 

>     
>     1 10 2
>     1 10 3
>     1 10 5
>     40 60 7
>     0 0 0
> 
> 

> 
> # Sample Output
> 
> 

>     
>     1,3,5,4,2,6,9,7,8,10
>     1,3,5,4,6,2,10,8,7,9
>     No anti-prime sequence exists.
>     40,41,43,42,44,46,45,47,48,50,55,53,52,60,56,49,51,59,58,57,54
> 
> 
</blockquote>


这题一看就是用回溯法，注意题目要求相邻2到p个数的和都是合数，代码如下：

[cpp]

#include <iostream>
using namespace std;

bool prime(int a) {//判断是否为质数
 int i = 0;
 for (i = 2; i * i <= a; i++) {
 if (a % i == 0)
 return false;
 }
 return true;
}

bool insert(int arr[], int a, int address, int d) {//判断数a能否作为arr[address]
 int i = 0, sum = a;
 for (i = address - 1; i > address - d && i >= 0; i--) {
 sum += arr[i];
 if (prime(sum))
 return false;
 }
 return true;
}

void judge(int arr[], bool used[], int n, int m, int d, int address, bool* ok) {
 int i = 0;
 for (i = n; i <= m; i++) {
 if (!used[i] && insert(arr, i, address, d)) {
 arr[address] = i;
 used[i] = true;
 if (address == m - n) {
 *ok = true;
 return;
 }
 judge(arr, used, n, m, d, address + 1, ok);
 if (*ok)
 return;
 used[i] = false;
 }
 }
}

int main() {
 int n, m, d, i;
 bool used[1001], ok = false;
 int arr[1001];
 while (cin >> n >> m >> d && n != 0) {
 ok = false;
 for (i = 0; i < 1001; i++)
 used[i] = false;
 judge(arr, used, n, m, d, 0, &ok);
 if (ok) {
 for (i = 0; i < m - n; i++)
 cout << arr[i] << ",";
 cout << arr[m - n] << endl;
 } else
 cout << "No anti-prime sequence exists." << endl;
 }
 return 0;
}

[/cpp]
