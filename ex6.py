#_*_coding:utf-8_*_
# 变量x ， 用10替换掉%d，格式化字符
x="There are %d types of people." % 10  #字符串包含字符串
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not) #字符串包含字符串

print x
print y

print "I said : %r." % x    #字符串包含字符串
print "I also said : '%s'" % y    #字符串包含字符串
hilarious = False
# 定义变量joke_evaluation ，其中包含一个未知的需格式化的类型%r
joke_evaluation = "Isn't that joke so funny?! %r !!!"   # 字符串包含字符串
# 打印joke_evaluation，把其中需格式化的%r 用变量hilarious的值进行替换，格式化输出
print joke_evaluation % hilarious    

w = "This is the left side of ..."
e= "a string with a right side. .... "

print w+e # 字符串连接