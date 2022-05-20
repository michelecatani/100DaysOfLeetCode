class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        resultSet = set()
        
        for i in nums1:
            if i in nums2:
                resultSet.add(i)
        
        return list(resultSet)