class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        theMin, theMax = 0, 0
        curMin, curMax = 0, 0
        answer = abs(nums[0])
        
        for i in nums:
            curMin = min(i, i + curMin)
            curMax = max(i, i + curMax)
            
            theMin = min(curMin, theMin)
            theMax = max(curMax, theMax)
            
            answer = max(theMax, abs(theMin))
            
        return answer