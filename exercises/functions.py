# Write your solution for 1.4 here!

def is_prime(x):
	number = int(x)
	for i in range (2, number-1):
		if i!=number-1:

			if number % i == 0:
				print("nope!, youre wrong")
				return("nope!, youre wrong")
		else:
			print("its a prime")
			return("its a prime")

	pass