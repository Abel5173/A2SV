class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def isPower(n):
            if n == 1:
                return True
            if n < 4:
                return False
            return isPower(n/4)
        return isPower(n)
    
