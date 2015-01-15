---
title: 算法设计期末考资料
layout: post
tags:
  - algorithm
---

为了应付考试整理了一些算法机考时参考。

**大数加减乘除乘方**

    #define SWAP(a,b) string c; c=a; a=b; b=c     //交換字符串
    int compare(string a, string b) {              //大數比較
      if (a.length() < b.length()) {
          return 0;
      } else if (a.length() == b.length()) {
          if (a < b)
              return 0;
      }
      return 1;
    }
    string add(string a, string b) {              //大數加法
      if (!compare(a, b)) {
          SWAP(a, b);
      }            //保證a的長度大於b
      int *ad = new int[a.length() + 1];
      memset(ad, 0, sizeof(int) * (a.length() + 1));  //初始化

      int i, j;
      for (i = 0; i < a.length() - b.length(); i++)    //將a長度大於b的部分傳過去
          ad[i + 1] = a[i] - '0';
      for (j = 0; i < a.length(); i++, j++)          //將a與b匹配的部分相加再傳
          ad[i + 1] = a[i] - '0' + b[j] - '0';
      for (i = a.length(); i > 0; i--) {             //進位操作
          if (ad[i] > 9) {
              ad[i - 1] += ad[i] / 10;
              ad[i] %= 10;
          }
      }
      char *c = new char[a.length() + 1];         //定義一個字符數組保存結果
      i = 0, j = 0;
      while (ad[i] == 0)
          i++;                      //去除前導0
      while (i < a.length() + 1)
          c[j++] = ad[i++] + '0';
      c[j] = '\0';
      if (c[0] == '\0') {
          c[1] = '\0';
          c[0] = '0';
      }     //如果結果为0
      free(ad);                                 //釋放ad數組
      string s(c);                              //將c轉換成string類型
      return s;
    }
    string subtract(string a, string b) {
      int flag = 0, i, j;
      if (!compare(a, b)) {                        //如果a<b，交換a、b並標識結果为負
          flag = 1;
          SWAP(a, b);
      }
      int *su = new int[a.length()];
      memset(su, 0, sizeof(int) * a.length());      //初始化
      for (i = 0; i < a.length() - b.length(); i++)    //將a長度大於b的部分傳過去
          su[i] = a[i] - '0';
      for (j = 0; i < a.length(); i++, j++)          //將a與b匹配的部分相減再傳
          su[i] = a[i] - b[j];
      for (i = a.length() - 1; i > 0; i--) {           //進位操作
          if (su[i] < 0) {
              su[i - 1]--;
              su[i] += 10;
          }
      }
      char *c = new char[a.length() + 2];
      i = 0, j = 0;
      if (flag)
          c[j++] = '-';                    //如果是負數，c[0]='-'
      while (su[i] == 0)
          i++;                      //後面同加法
      while (i < a.length())
          c[j++] = su[i++] + '0';
      c[j] = '\0';
      if (c[0] == '\0') {
          c[1] = '\0';
          c[0] = '0';
      }
      free(su);
      string s(c);
      return s;
    }
    string multiply(string a, string b) {
      int *mu = new int[a.length() + b.length()];
      memset(mu, 0, sizeof(int) * (a.length() + b.length()));
      for (int i = 0; i < a.length(); i++)                 //將數字兩兩相乘
          for (int j = 0; j < b.length(); j++)
              mu[i + j + 1] += (a[i] - '0') * (b[j] - '0');
      for (int i = a.length() + b.length() - 1; i > 0; i--) {  //進位操作
          if (mu[i] > 9) {
              mu[i - 1] += mu[i] / 10;
              mu[i] %= 10;
          }
      }
      char *c = new char[a.length() + b.length()];
      int i = 0, j = 0;

      while (mu[i] == 0)
          i++;
      while (i < a.length() + b.length())
          c[j++] = mu[i++] + '0';
      c[j] = '\0';
      if (c[0] == '\0') {
          c[1] = '\0';
          c[0] = '0';
      }
      free(mu);
      string s(c);
      return s;
    }
    string *devide(string a, string b) {
      string *de = new string[2];
      de[0] = "0";
      de[1] = b;
      string one = "1", ten = "10";
      if (!compare(a, b))
          return de;
      while (a[0] != '-') {
          de[1] = a;
          a = subtract(a, b);
          de[0] = add(de[0], one);
      }
      de[0] = subtract(de[0], one);
      return de;
    }
    string power(string a, string b) {
      string c = "1", one = "1";
      while (b[0] != '0') {
          c = multiply(c, a);
          b = subtract(b, one);
      }
      return c;
    }

**大数求模**

    int BigNumMod(char bigNum[], int b) {
      int mod = 0;
      for (int j = 0; j < strlen(bigNum); j++) {
          mod = (bigNum[j] - '0' + 10 * mod) % b;
      }
      return mod;
    }

**快速取模(a pow b mod c)**

    int PowerMod(int a, int b, int c)
    {
      int ans = 1;
      a = a % c;
      while(b>0) {
          if(b % 2 = = 1)
          ans = (ans * a) % c;
          b = b/2;
          a = (a * a) % c;
      }
      return ans;
    }

**筛法求素数**

    #define MAXPRIME 1000000
    int prime[MAXPRIME];
    int testPrime(int n, int i) {
        int k = n;
        for (int j = 0; j < i; j++) {
            if (prime[j] > k)
                break;
            if (n % prime[j] == 0)
                return 0;
            k = n / prime[j];
        }
        return 1;
    }
    void getPrime() {
        int i = 1;
        prime[0] = 2;
        for (int n = 3; n < MAXPRIME; n++) {
            if (testPrime(n, i)) {
                prime[i] = n;
                i++;
                if (i >= MAXPRIME)
                    break;
            }
        }
    }

**全排列**

    while (next_permutation(str.begin(), str.end()))
    {
        cout << str << endl;
    }

**康拓展开**

排列与整数之间的映射

    int fac[] = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 }; //阶乘
    int cantor(int *s, int n) {
        int num = 0;
        for (int i = 0; i < n - 1; i++) {
            int tmp = 0;
            for (int j = i + 1; j < n; j++)
                if (s[j] < s[i])
                    tmp++;
            num += fac[n - i - 1] * tmp;
        }
        return num;
    }

    void _cantor(int *s, int n, int x) {
        bool tmp[n + 1];
        memset(tmp, 0, sizeof(tmp));
        for (int i = n - 1; i >= 0; i--) {
            int k = x / fac[i];
            x %= fac[i];
            int j = 1;
            for (int sum = 0; sum < k || tmp[j]; j++)
                if (!tmp[j])
                    sum++;
            s[n - 1 - i] = j;
            tmp[j] = 1;
        }
    }
