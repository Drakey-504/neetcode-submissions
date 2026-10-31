class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        res = r

        while l<=r:

            k = l + (r-l)//2
            cur_hrs = 0
            for i in range(len(piles)):
                cur_hrs += math.ceil(piles[i]/k)

            if cur_hrs > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res               