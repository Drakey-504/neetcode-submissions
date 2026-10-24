class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += f"{len(s)}#{s}"   
        return en    

    def decode(self, s: str) -> List[str]:
        print(f"Source string:{s}")
        if s == "":
            return []
        res = []    
        i = 0
        while i < len(s):
            s_len = ""
            while s[i] != "#":
                s_len += s[i]
                i+=1
            print(f"Word string length:{s_len}")   
            i+=1
            res.append(s[i:i+int(s_len)])
            i = i + int(s_len)

        return res    

                
