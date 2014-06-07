
##############################
def a(x,y):
	return x**y

print "def 2**3 = " + str(a(2,3))

###################################
f = lambda x: x+1

print "lambda 3+1 = "+ str(f(3))

#####################################

f_2 = lambda x,y: x**y

print "lambda 2**3 = " + str(f_2(2,3))

#####################################

def add(n):
	return lambda x: x+n


add_ = add(3)

print "enbedded lambda add(10) = " + str(add_(10))

###################################





