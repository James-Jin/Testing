import time
start_time = time.time()
def natural_series_400():
	temp = 0.0
	x = 1
	while(temp<400):
		temp +=  1.0/x
		if (x %10000000 == 0):
			print "we reach",x
			print "sum = ",temp
			print "time:", (time.time()- start_time)
		x +=1
		
	print "n is",x
	return temp
	
print "result is {0}," .format(natural_series_400())
