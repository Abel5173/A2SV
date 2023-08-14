class Solution:
    def countGoodNumbers(self, n: int) -> int:
	  # Reusing the super power logic 
	  # to calculate pow(x,n)%mod
      def myPow(x: int, n: int, mod: int) -> int:
        if n == 0:
          return 1
        elif n == 1:
          return x
        else:
          half = myPow(x, n//2,mod)
          if n % 2 == 0:
			# Eg: n = 4 we can split into 2 and 2
			# so we multiply two halves alone
            return (half*half)%mod
		  # Eg: n = 5 we get n//2 = 2 
          # which we can split into 2,2,1
		  # so we multiply the halves twice and multiply the x for once
          return ((half*half)%mod*x)%mod
      
      # For an odd length string we get n//2+1 odd indices and n//2 even indices
      # For an even length string we get n//2 odd indices and n//2 even indices
      if n%2 == 0:
        return ((myPow(4,n//2,10**9+7))*(myPow(5,n//2,10**9+7)))%(10**9+7)
      return ((myPow(4,n//2,10**9+7))*(myPow(5,1+n//2,10**9+7)))%(10**9+7)
    
print(Solution().countGoodNumbers(4))