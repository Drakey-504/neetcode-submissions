class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:

            c_count = [0] * 26
            for c in s:
                c_count[ord(c)-ord('a')] += 1

            dict_key = tuple(c_count)

            if dict_key not in groups:
                groups[dict_key] = []

            groups[dict_key].append(s)    

        return [v for v in groups.values()]                    