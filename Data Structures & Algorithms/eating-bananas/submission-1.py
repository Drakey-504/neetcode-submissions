class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        res = -1

        while l<=r:

            k = l + (r-l)//2
            cur_hrs = 0
            for i in range(len(piles)):
                cur_hrs += math.ceil(piles[i]/k)

            if cur_hrs > h:
                l = k + 1
            else:
                if res == -1:
                    res = k
                else:
                    res = min (res, k)
                r = k - 1

        return res               