#!/usr/bin/python
#coding=utf-8
#建立一个record.txt的文档，写入内容如下,再从 record.txt 中读取文件并打印。
#tom, 12, 86
#Lee, 15, 99
#Lucy, 11, 58
#Joseph, 19, 56
#---------------------------------------------------------------------------

f=open('record.txt','w')
f.writelines('tom,12,86\nlee,15,99\njoseph,19,56')
f.close()
x=open('record.txt','r')
content=x.read()
x.close()
print content

