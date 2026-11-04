class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        nlen = len(nums)
        prod_left = [1] * nlen
        prod_right = [1] * nlen

        r = nlen-2
        for l in range(1, nlen):
            prod_left[l] = prod_left[l-1] * nums[l-1]
            prod_right[r] = prod_right[r+1] * nums[r+1]
            r -= 1

        res = [1] * nlen

        for i in range(nlen):
            res[i] = prod_left[i]*prod_right[i]

        return res    

