class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        canReach = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= canReach:
                canReach = i
        
        return canReach == 0