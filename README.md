# monitors


[![Build Status](https://travis-ci.com/Pactortester/monitors.svg?branch=master)](https://travis-ci.com/Pactortester/monitors) ![PyPI](https://img.shields.io/pypi/v/monitors) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/monitors) ![GitHub top language](https://img.shields.io/github/languages/top/Pactortester/monitors) ![PyPI - Downloads](https://img.shields.io/pypi/dm/monitors) ![GitHub stars](https://img.shields.io/github/stars/Pactortester/monitors?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)


## Logo


![logo](images/monitors.png)


## 安装


pip install monitors


##  仓库地址：


- github：https://github.com/Pactortester/monitors.git
- pypi：https://pypi.org/project/monitors/#history


## 社区地址


- testerhome：https://testerhome.com/opensource_projects/monitors


## 适用场景


1. 监控某一个进程的性能,默认监控一天，数据每隔3秒刷新一次
2. 根据子进程名称获取到父进程的id,进行性能监控。
3. 适用于各个平台（Windows, Mac, Linux）
- 例如：想监控整个chrome浏览器的系统资源消耗情况
- 只需要传入[chrome.exe] 系统将自动为你监控整个chrome浏览器的资源消耗情况。
## 
![chrome.exe](images/example.png)


## 功能


1. 自动监控此进程的性能情况，控制台实时输出数据
2. 将性能数据以log文件形式存与 [monitor_log] 文件夹



## 命令


```shell
python <you_test_script.py>
```


## Demo


```python
from monitors.monitor_util import monitor_start

monitor_start(name='chrome.exe')
```
## 

以上便是 monitors 的基本用法介绍。

如果您有发现错误，或者您对 monitors 有任何建议，欢迎到 [monitors Issues](https://github.com/Pactortester/monitors/issues) 发表，非常感谢您的支持。您的反馈和建议非常宝贵，希望您的参与能帮助 monitors 做得更好。
