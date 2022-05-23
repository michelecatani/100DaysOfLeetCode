class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        greater, lesser, answer = 1, 1, 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                greater = lesser + 1
                lesser = 1
            elif arr[i] < arr[i-1]:
                lesser = greater + 1
                greater = 1
            else:
                lesser, greater = 1, 1
        
            answer = max(lesser, greater, answer)
        
        return answer