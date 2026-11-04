class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""

        for s in strs:
            res = res + f"{len(s)}#{s}"

        return res    

    def decode(self, s: str) -> List[str]:

        res = []
        i=0
        while i < len(s):
            cnt_string = ""
            while s[i]!= "#":
                cnt_string += s[i]
                i += 1

            cnt = int(cnt_string)   
            i += 1

            res.append(s[i:i+cnt])    
            i += cnt

        return res    