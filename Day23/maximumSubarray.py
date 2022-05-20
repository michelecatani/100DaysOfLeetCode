class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = float('-inf')
        theMax = float('-inf')
        
        for i in nums:
            cur = max(i, i + cur)
            theMax = max(cur, theMax)
            
        return theMax