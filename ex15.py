#_*_coding:utf-8_*_

from sys import argv

script , filename = argv
# 打开用户输入的文件，open函数获取到用户输入的文件名的文件
txt = open(filename)

print "Here is your file %r:" % filename
# 读取文件并打印在控制台上
print txt.read()
txt.close
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open (file_again)

print txt_again.read()
txt_again.close