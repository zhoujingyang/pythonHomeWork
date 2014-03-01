# _*_coding:utf-8_*_

# 声明一个函数cheese_and_crackers，这个函数接受两个参数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
print "We can just give the function numbers directly:"

# 调用cheese_and_crackers函数，将20和30当做参数传递进去
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# 调用cheese_and_crackers函数，将amount_of_cheese, amount_of_crackers两个变量的值传递进去
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
print "We can even do math inside too:"
# 调用cheese_and_crackers函数，将10 + 20与5 + 6的结果当做参数传递进去
cheese_and_crackers(10 + 20, 5 + 6)
print "And we can combine the two, variables and math:"
# 调用cheese_and_crackers函数，将amount_of_cheese + 100和 amount_of_crackers + 1000当做参数传递进去
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




