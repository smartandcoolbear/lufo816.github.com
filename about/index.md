---
title: About
layout: page
comments: yes
---


##基本信息

- Github: [github.com/lufo816](https://github.com/lufo816)
- 电子邮件: [lufo816@gmail.com](mailto:lufo816@gmail.com)
- 教育经历: 2012级中山大学移动信息工程学院软件工程专业本科
- 技能:熟悉Python,C,C++,长期使用Linux/Unix操作系统
	
##实习经历
- 2015.7至今:于中国科学院重庆研究院[智能多媒体技术研究中心](http://www.cigit.cas.cn/jggk/ggkypt/201403/t20140328_4082809.html)人脸识别组([云从科技](http://www.cloudwalk.cn/)研发组)实习,工作内容包括:
	- 进行实验:对比不同Alignment算法对人脸识别性能的影响,并提出改进方案
	- 完善深度学习代码:尝试将PLDA算法作为loss function写入caffe的源代码中.尝试设计CNN完成图片去模糊的工作
	- 数据抓取:完成爬虫抓取百度,人人,bing等网站的图片并进行自动筛选,部署到多台机器上,目标是抓取数十TB的数据,整理后将获得比现有数据集大至少一个数量级的数据集
- 2014.3-2015.7:中山大学移动信息工程学院软件设计和操作系统的教学助理

##论文发表
- **Xuebo Liu**, Shuang Ye, Yonghao Luo, Yanghui Rao, [ZhihuRank: A Topic-Sensitive Expert Finding Algorithm in Community Question Answering Websites](http://lufo.me/docs/ZhihuRank.pdf), [International Conference on Web-based Learning (ICWL) 2015](http://www.cityu.edu.hk/merc/icwl/icwl2015home.htm)
- 
- Shuang Ye, KaiChun Lin, XinYi Lin, **XueBo Liu**, Chang-Dong Wang, HanChen Yu, Schedule Management Application ‘WiDay’ based on SAE cloud platform, [IEEE International  Conference on Big Data and Cloud Computing 2015](http://www.cybermatics.org/SWC2015/CBD/CBD2015.htm)


##项目经历

- **机器学习**
	- ZhihuRank:问答类社交网站中专家推荐创新算法,在社交类问答网站(知乎,Quora)中基于用户与问题间的主题相似度和用户间的赞同关系对每个问题推荐最适合回答这个问题的用户.算法基于LDA和PageRank,从知乎上抓取了超过20万条答案进行实验,效果比同类算法提高2%-10%,以第一作者完成论文并发表在ICWL 2015
	- [语音识别系统](https://github.com/lufo816/SpeechRecognitionSystem):完成基于GMM和HMM的语音识别系统,可以识别特定的连续语音,如电话号码,单个数字的识别准确率超过90%,电话号码的识别准确率超过80%.使用MFCC作为特征,HMM中的每个state使用GMM表示,以word为单位进行识别,训练数据很少,增加数据可提升效果
	- [TwitterRank](https://github.com/lufo816/TwitterRank):提取各个主题下最有影响力的Twitter用户,使用LDA算法提取主题,抓取Twitter上粉丝数前100的用户数据完成实验
- **其他**
	- [基于Flask框架的微信公众号二维码管理网站](https://github.com/lufo816/WeiXinPublicAccountFollowedByQRAnalysis):方便微信公众号管理二维码的网站.个人负责基于FLask框架进行后台开发,使用MySQL储存数据
	- [基于webpy框架查菜谱微信公共号](https://github.com/lufo816/WeiXinCookbook):用户可在公众号中查询各种菜的做法,基于webpy框架进行开发,使用MySQL储存数据,调用聚合数据的API获取菜的做法,完成静态网页生成器将json格式的数据转化为网页推送给用户
	- 最流行的[知乎民间 API](https://github.com/egrcc/zhihu-python)(Github上有超过500个stars):可以获取知乎的各种数据,使用requests库发送请求,使用BeautifulSoup对网页源码进行解析.个人负责修改Bug,添加功能,如获取每个答案赞同人列表等
	
-----

如果这个博客对您有所帮助，您可以扫描下面的二维码请我喝杯咖啡:

手机微信扫一扫下方的二维码可以直接付款
![](/media/files/2015/07/09.jpg =256x256) 
