class primeFactors(object):
	def __init__(self):
		self.__primes = []

	def generate(self,n):
		if n > 1:
			self.__primes.append(2)
		return self.__primes
