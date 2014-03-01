#_*_coding:utf-8_*_

from sys import argv

script,filename=argv

print "We'are going to erase %r." % filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that ,hit RETURN"

raw_input("?")

print "Opening the file ......."
# 获取文件以及写文件的权限
target = open(filename , 'w')

print "Truncating the file . Goodbye!!!!"
# 清空文件
target.truncate()#这一行加不加都可以，因为文件以w权限打开时，就已经被清空了

print "Now I'm going to ask you for three lines."
# 获取用户输入
line1 = raw_input("line 1 :")
line2 = raw_input("lin3 2 :")
line3 = raw_input("line 3 :")
print "I'm going to write these to the file ."
# 写文件
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()


