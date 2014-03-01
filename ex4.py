#_*_coding=utf-8_*_

# 定义一个变量car  值为整型100
cars=100
# 定义一个变量space_in_a_cat 值为浮点型数值4.0
space_in_a_car=4.0

drivers=30

passengers=90
# 定义一个变量cars_not_driven 值为变量cats的值减去变量drivers的值的差
cars_not_driven=cars-drivers
# 定义一个变量cars_driven 等于变量drivers的值
cars_driven = drivers
# 定义一个变量carpool_capacity 等于cars_driven与space_in_a_car的乘积
carpool_capacity=cars_driven*space_in_a_car
#定义一个变量average_passengers_per_car 等于passengers与cars_driven的 商
average_passengers_per_car=passengers/cars_driven

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "we need to put about",average_passengers_per_car,"in each car."


