class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        
        answer1, answer2 = 0, 0
        prevHouseTotal, secondPrevHouseTotal = 0, 0
        
        for i in range(len(nums) - 1):
            temp = max(prevHouseTotal, secondPrevHouseTotal + nums[i])
            secondPrevHouseTotal = prevHouseTotal
            prevHouseTotal = temp
        
        answer1 = prevHouseTotal
        
        prevHouseTotal, secondPrevHouseTotal = 0, 0
        
        for i in range(1, len(nums)):
            temp = max(prevHouseTotal, secondPrevHouseTotal + nums[i])
            secondPrevHouseTotal = prevHouseTotal
            prevHouseTotal = temp
            
        answer2 = prevHouseTotal
        
        return max(answer1, answer2)