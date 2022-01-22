class primes:
    def __init__(self, nlimit):
        self.nlimit = nlimit
        self.is_prime = [True] * nlimit
        self._sieve()
        self.next = 1

    def __iter__(self):
        return self

    def _sieve(self):
        self.is_prime[0] = False 
        self.is_prime[1] = False
        for i in range(2, int(self.nlimit**0.5)+1):
            if self.is_prime[i]:
                for j in range(i*i, self.nlimit, i):
                    self.is_prime[j] = False

    def __next__(self):
        n = self.next + 1

        while True:
            if n >= self.nlimit:
                raise StopIteration
            elif self.is_prime[n]:
                self.next = n
                return self.next    
            else:
                n += 1


list(primes(100000))