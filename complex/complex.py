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

###############################
use isinstance() instead of type()

################################################

# so what happens when we take the union of that?
u = set().union(result_y)
s = set(result_y)
print u
#set([16, 25, 4, 36])
print s
#set([16, 25, 4, 36])

################################################
f(*C)
# is the same as x, y, z = C
f(x, y, z)
# The * says "make it as if the elements of this collection each appear 
# as a separate argument of the function call", which is what we want.

# We could also do this without * and without union as follows: replace

set().union( *map(y, x(text))
#with
set(yrem for xrem in x(text) for yrem in y(xrem))
########################################################
 
