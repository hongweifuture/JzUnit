# 介绍
用Python搭建自动化测试框架，需要组织用例以及测试执行，我使用的是Python的标准库unittest，借鉴了部分nose

## 基础
[Python自动单元测试框架介绍](https://www.ibm.com/developerworks/cn/linux/l-pyunit/)

[单元测试框架基础](http://pyunit.sourceforge.net/pyunit_cn.html)

[深入理解unittest](https://huilansame.github.io/huilansame.github.io/archivers/python-unittest)

## 流程
1. 自动运行cases文件夹下的测试用例
1. 合并结果生成htnl测试报告
1. 将报告发送到指定邮箱（附件自定义）

## 特点
- 参数化配置
- 完整测试用例放在框架内直接执行
- 记录日志输出，配置文件控制，可记录多个
- 自动生成易读测试报告
- 报告自动发送

# 目录结构
![Markdown](http://i4.buimg.com/1949/97a6692dd0e672bf.png)

文件/文件夹 | 说明
--|--
startup.py | 启动程序
cases | 测试用例
config | 配置文件
log | 日志存放
report | 报告存放
src | 封装的库类

# 配置文件示例
![link](http://img.blog.csdn.net/20161115111152671)

# 报告示例
![报告](http://img.blog.csdn.net/20161115112653271)

![详情](http://i1.piimg.com/1949/4118881b44ddc983.png)

# 后续
- 配置文件换成yaml或json
- 加入数据驱动
- 继续完善







