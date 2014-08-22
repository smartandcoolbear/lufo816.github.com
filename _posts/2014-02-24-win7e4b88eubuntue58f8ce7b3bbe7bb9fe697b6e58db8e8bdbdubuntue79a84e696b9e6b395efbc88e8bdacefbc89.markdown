---
author: lufo
comments: true
date: 2014-02-24 03:29:48+00:00
layout: post
slug: win7%e4%b8%8eubuntu%e5%8f%8c%e7%b3%bb%e7%bb%9f%e6%97%b6%e5%8d%b8%e8%bd%bdubuntu%e7%9a%84%e6%96%b9%e6%b3%95%ef%bc%88%e8%bd%ac%ef%bc%89
title: Win7与Ubuntu双系统时卸载Ubuntu的方法（转）
wordpress_id: 159
categories:
- 小Tips
---

转自：http://www.linuxidc.com/Linux/2010-03/25129.htm

1. 下载[MBRFix](http://www.linuxidc.com/Linux/2007-11/8785.htm)工具，放在c盘，利用命令提示符，进入软件所在目录，cd c:\mbrfix    （cd后面一个空格）

2.输入 MBRFix /drive 0 fixmbr /yes

3.重启，发现直接进入Win 7，现在可以用Win 7的磁盘管理（打不开的话，可以用Win 7优化大师里带的）格式化[Ubuntu](http://www.linuxidc.com/topicnews.aspx?tid=2)所在分区（就是没有盘符的，选定删除卷时会提示是其他系统的数据）了~~~

---------------------------------

如果直接在Win 7里面删除Ubuntu所在的分区，则由于grub也被删除了，导致无法引导Win 7,可以使用安装光盘在dos命令下执行fdisk /mbr修复引导区，下面说说没有安装光盘之类的进入dos的解决办法。

下载[MBRFix](http://www.linuxidc.com/Linux/2007-11/8785.htm),把mbrfix.exe复制到c盘根目录下，在cmd里面运行mbrfix /dirve 0 fixmbr /yes, 如果出现error:5,则右击mbrfix.exe选择属性将mbrfix的兼容性改为以管理员身份运行。

然后重启一遍，到Win 7下面在磁盘管理里面将Ubuntu所占用的分区删除即可
