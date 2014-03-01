print "\\\\","\\\'","\\a","\\b",
print "\\f","\\n","\\N","\\r",
print "\\t","\\\u","\\\U"

es = '''
\tThis
\tis
\tmy
\ttest
'''
print es

es_1 = "first test ,%r"

print es_1 % es

es_2 = "This is string ,the users should be looked %s"

print es_2 % es