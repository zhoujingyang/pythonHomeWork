#_*_coding=utf-8_*_

# ����һ������car  ֵΪ����100
cars=100
# ����һ������space_in_a_cat ֵΪ��������ֵ4.0
space_in_a_car=4.0

drivers=30

passengers=90
# ����һ������cars_not_driven ֵΪ����cats��ֵ��ȥ����drivers��ֵ�Ĳ�
cars_not_driven=cars-drivers
# ����һ������cars_driven ���ڱ���drivers��ֵ
cars_driven = drivers
# ����һ������carpool_capacity ����cars_driven��space_in_a_car�ĳ˻�
carpool_capacity=cars_driven*space_in_a_car
#����һ������average_passengers_per_car ����passengers��cars_driven�� ��
average_passengers_per_car=passengers/cars_driven

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "we need to put about",average_passengers_per_car,"in each car."


