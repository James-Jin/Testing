# def cheese_and_crackers(cheese_count,box_of_crackers):
	# print "you have %d cheeses" %cheese_count
	# print "you have %d boxes of crackers" %box_of_crackers
	# print "man, that are enough for a party@!"
	# print "Get a blanket.\n"
	
# print "We can just give the function numbers directly."
# cheese_and_crackers(20,30)

# print "OR, we can use variables from our script:"
# amount_of_cheese = 100
# amount_of_crackers = 200
# cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# print "We can even do math inside too"
# cheese_and_crackers(10+5,10/2)

# print "And we can combine the two, variables with math"
# cheese_and_crackers(amount_of_cheese+10,amount_of_crackers*2)




# def factory(number):
	# temp=1
	# for x in range (0,number):
		# temp = temp*(x+1)
	# return temp
	
# user_input = input("number to calculate:")
# print "factory of %d is : %d" %(user_input,factory(user_input))


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
