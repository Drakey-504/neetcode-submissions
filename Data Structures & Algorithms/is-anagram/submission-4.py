class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hmp = [0] * 26
        t_hmp = [0] * 26

        temp = 0

        for c in s:
            temp = ord(c) - 97
            s_hmp[temp] = s_hmp[temp] + 1

        for c in t:
            temp = ord(c) - 97
            t_hmp[temp] = t_hmp[temp] + 1

        for i in range(26):
            if s_hmp[i] != t_hmp[i]:
                return False

        return True            
            