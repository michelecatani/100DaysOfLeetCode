class Solution:    
    def maxProduct(self, nums: List[int]) -> int:
        theMin, theMax = 1, 1
        answer = nums[0]
        
        for i in nums:
            
            curs = (i, i * theMin, i * theMax)
            theMin = min(curs)
            theMax = max(curs)
            
            answer = max(answer, theMax)
        
        return answer