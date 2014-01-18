def isPrime(n):
	"""Checks if n is prime"""
	#Check for obvious True or False before entering loop, for efficiency.
	if n <= 1 or type(n) != int:
		##A prime must be a positive whole number.
		##1 is not a prime
		return False

	if n in [2, 3, 5, 7, 11, 13, 17, 19]:
		##Quick check of the first few primes.
		return True

	if not n & 1:
		##Check to see if n is even.
		##2 is the only even prime.
		return False

	siftr = int(n**0.5)  ##Only the first sqrt(n), any more is redundant.
	ctr = 3             ##Start the counter at 11, the next known prime.
	#Enter loop to check all other possibilities.
	while ctr <= siftr:
		if n % ctr == 0:  ##Test if ctr is a multiple of n.
			return False
		ctr += 2            ##Only need to check the odd numbers.
	return True

def areBothPal(n):
    nBin = bin(n).replace('0b', '')
    n = str(n)
    if n == n[::-1] and nBin == nBin[::-1]:
        return True
    else:
        return False

counter = 11
while counter >= 11:
    if isPrime(counter):
        isPal = areBothPal(counter)
        if isPal:
            a = counter
            break
    counter += 1

print (a, bin(a))


##a = 11
##while True:
##    B = lambda x: bin(a)[2:]
##    if isPrime(a) and str(a)==str(a)[::-1] and B(a) == B(a)[::-1]:
##        print ("base-10: " + str(a))
##        print ("base-2: " + B(a))
##        break
##    a+=2
