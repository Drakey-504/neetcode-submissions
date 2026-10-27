class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        f = 0
        b = len(s) - 1

        while f < b:
            while f < b and not s[f].isalnum():
                f += 1
            while f < b and not s[b].isalnum():
                b -= 1

            if s[f].lower() != s[b].lower():
                return False

            f += 1
            b -= 1

        return True                