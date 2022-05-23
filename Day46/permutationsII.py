##i copped out hard here as well!!

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        s = set(itertools.permutations(nums))
        
        return list(s)