integer = int(raw_input("Enter a positive integer: "))
for divisor in range(1, integer + 1):
	if integer % divisor == 0:
		print "{} is a divisor of {}".format(divisor, integer)