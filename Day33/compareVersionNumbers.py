class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        for i in range(len(v1)):
            v1[i] = int(v1[i])
        
        for i in range(len(v2)):
            v2[i] = int(v2[i])
        
        length = max(len(v1), len(v2))
        
        for i in range(length):
            if i >= len(v2):
                if v1[i] > 0:
                    return 1
            elif i >= len(v1):
                if v2[i] > 0:
                    return -1
            else:
                if v1[i] > v2[i]:
                    return 1
                if v1[i] < v2[i]:
                    return -1
        
        return 0