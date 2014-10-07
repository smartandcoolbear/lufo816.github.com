---
author: lufo
comments: true
date: 2014-03-10 14:48:20+00:00
layout: post
slug: windows%e4%b8%8bpython%e8%be%93%e5%87%ba%e4%b9%b1%e7%a0%81%e9%97%ae%e9%a2%98
title: windows下python输出乱码问题
wordpress_id: 171
tags:
- 小Tips
---

python代码编码为utf-8时输出会自动变为utf-8，与cmd和IDIE的默认编码不同会出现乱码，所以应加上：

[python]

import sys
type = sys.getfilesystemencoding()
print myname.decode('UTF-8').encode(type)

[/python]

参考：[http://www.cnblogs.com/frankfang/archive/2011/11/02/2233661.html](http://www.cnblogs.com/frankfang/archive/2011/11/02/2233661.html)
