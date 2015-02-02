# PdfKit

鉴于网上不少影印的PDF没有目录，自己暂时还没找到一个小工具自动生成目录的，就做了这个PdfKit 
## 功能
1. 合并PDF
2. 为PDF生成目录

## 使用说明
1. 如果是生成书签，则至少说明目录所在页数和内容第一页所在页数，输出原pdf的副本文件（*_copy.pdf）
2. 如果合并pdf，则按顺序说明被合成的pdf所在路径，输出merge.pdf
<br>
![image](https://raw.githubusercontent.com/zhuzhenpeng/PdfKit/master/images/help.jpg) 

## 效果图
![image](https://raw.githubusercontent.com/zhuzhenpeng/PdfKit/master/images/result.jpg)

## 运行注意事项：
1. 需要PyPDF2 (1.23)库
2. 需要docopt (0.6.2)库
3. 进入pdf目录后，执行pk.py文件即可看到基本的命令, pk -h 进一步查看命令
