def factorial(number):
	""" Calculate the factorial of a number """

	x = 1
	while number >= 1:
		x = x * number
		number = number - 1
	return (x)