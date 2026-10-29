class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        cf_s1 = [0] * 26
        cf_s2 = [0] * 26

        for s in s1:
            cf_s1[ord(s)-ord('a')] += 1

        l=0
        for r in range(len(s2)):
            cf_s2[ord(s2[r])-ord('a')] += 1

            if r-l+1 > len(s1):
                cf_s2[ord(s2[l])-ord('a')] -= 1
                l += 1

            if cf_s1 == cf_s2:
                return True    

        return False