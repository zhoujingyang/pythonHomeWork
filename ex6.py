#_*_coding:utf-8_*_
# ����x �� ��10�滻��%d����ʽ���ַ�
x="There are %d types of people." % 10  #�ַ��������ַ���
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not) #�ַ��������ַ���

print x
print y

print "I said : %r." % x    #�ַ��������ַ���
print "I also said : '%s'" % y    #�ַ��������ַ���
hilarious = False
# �������joke_evaluation �����а���һ��δ֪�����ʽ��������%r
joke_evaluation = "Isn't that joke so funny?! %r !!!"   # �ַ��������ַ���
# ��ӡjoke_evaluation�����������ʽ����%r �ñ���hilarious��ֵ�����滻����ʽ�����
print joke_evaluation % hilarious    

w = "This is the left side of ..."
e= "a string with a right side. .... "

print w+e # �ַ�������