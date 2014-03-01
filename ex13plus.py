#_*_coding:utf-8_*_

# 错误信息如下：
# Traceback (most recent call last):
#  File "ex13.py", line 3, in <module>
#    script, first, second, third = argv
# ValueError: need more than 3 values to unpack
# ex13.py 的第三行有错，需要的解包参数不仅仅是3个


from sys import argv

FileName,YourName = argv

print "The filename is:",FileName
print "your name is %s" % YourName



