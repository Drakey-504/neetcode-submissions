class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        if n == 1:
            return s

        res = 0
        indices = -1,-1

        isPal = [[False] * n for _ in range(n)]

        for sub_len in range(1,n+1):
            l = 0
            r = l + sub_len - 1

            while r < n:
                if isPal[l][r]:
                    l += 1
                    r += 1
                    continue
                else:
                    if sub_len == 1:
                        isPal[l][r] = True
                    elif sub_len == 2:
                        isPal[l][r] = True if s[l] == s[r] else False
                    else:
                        if s[l] == s[r] and isPal[l+1][r-1]:
                            isPal[l][r] = True
                    if isPal[l][r] and res < sub_len:
                        res = sub_len
                        indices = l, r
                    l += 1
                    r += 1        

        return s[indices[0]:indices[1]+1]