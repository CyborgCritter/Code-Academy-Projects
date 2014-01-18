def isPrime(n):
	"""Checks if n is prime"""
	#Check for obvious True or False before entering loop, for efficiency.
	if n <= 1 or type(n) != int:
		##A prime must be a positive whole number.
		##1 is not a prime
		return False

	if n < 20 and n in [2, 3, 5, 7, 11, 13, 17, 19]:
		##Quick check of the first few primes.
		return True

	if not n & 1:
		##Check to see if n is even.
		##2 is the only even prime.
		return False

	sifter = int(n**0.5)  ##Only the first sqrt(n), any more is redundant.
	counter = 11             ##Start the counter at 11, the next known prime.
	#Enter loop to check all other possibilities.
	while counter <= sifter:
		if n % counter == 0:  ##Test if ctr is a multiple of n.
			return False
		counter += 2            ##Only need to check the odd numbers.
	return True
