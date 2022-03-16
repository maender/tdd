def fizzbuzz(n):
	out = ''
	if n % 15 == 0: out = 'FizzBuzz'
	elif n % 3 == 0: out = 'Fizz'
	elif n % 5 == 0: out = 'Buzz'
	else: out = str(n)
	return out