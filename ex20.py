#_*_coding:utf-8_*_

from sys import argv

script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count,f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print ("Now let's rewind,kind of like a tape.")
rewind(current_file) #定位文件的位置，根据函数的功能，表示从第0位开始读
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)


i=3
j=2
j+=i
print j