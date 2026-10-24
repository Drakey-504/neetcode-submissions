class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:

            c_count = [0] * 26
            for c in s:
                c_count[ord(c)-ord('a')] += 1

            groups[tuple(c_count)].append(s)    

        return [v for v in groups.values()]                    