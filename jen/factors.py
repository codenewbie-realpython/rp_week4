# real python week 4 chap 8 - jen b

num = int(raw_input("Enter a positive integer: "))
for divisor in range(1, num+1):
    if num % divisor == 0:
        print "{} is a divisor of {}".format(divisor, num)
