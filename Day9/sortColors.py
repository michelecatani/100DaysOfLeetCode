class Solution:
    
    def swap(self, nums: List[int], i, j):
        
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        
        while j <= k:
            
            if nums[j] < 1: 
                self.swap(nums, i, j)
                i += 1
                j += 1
            elif nums[j] > 1:
                self.swap(nums, j, k)
                k -= 1
            else:
                j += 1