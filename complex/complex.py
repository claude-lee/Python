#What does set().union(*map(y, x(text))) do?
# let's start with the mapping:
# you map a function with a list

list_x = [2,4,5,6]
print "list is :      " + str(list_x)
def func_xp(a):
	return a**2
print "func is square"

result_y = map(func_xp, list_x)
print "map(func_xp, list_x)"
print "unreadable: " + str(result_y) # unreadable
# weird that it is readable

readable_result_z = list(result_y)

print str(readable_result_z)
