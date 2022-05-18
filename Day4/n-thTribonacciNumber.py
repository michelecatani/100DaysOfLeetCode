class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = [-1] * 38
        
        def trib(n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            
            if memo[n] != -1:
                return memo[n]
            
            else:
                memo[n] = trib(n-1) + trib(n-2) + trib(n-3)
                return memo[n]
        
        return trib(n)