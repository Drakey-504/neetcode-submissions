class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False
        
        matched_freq = 0
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for i in range(len(s1)):           
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            matched_freq += (1 if s1_freq[i] == s2_freq[i] else 0)    

        l = 0
        for r in range(len(s1), len(s2)):
            if matched_freq == 26:
                return True

            index_r = ord(s2[r]) - ord('a')

            s2_freq[index_r] += 1

            if s2_freq[index_r] == s1_freq[index_r]:
                matched_freq += 1
            elif s2_freq[index_r] == s1_freq[index_r] + 1:
                matched_freq -= 1

            index_l = ord(s2[l]) - ord('a')
            s2_freq[index_l] -= 1           
            l += 1    

            if s2_freq[index_l] == s1_freq[index_l]:
                matched_freq += 1
            elif s2_freq[index_l] + 1 == s1_freq[index_l]:
                matched_freq -= 1   

        return matched_freq == 26         
