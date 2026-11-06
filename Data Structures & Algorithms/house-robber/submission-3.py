class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])

        nums[-2] = max(nums[-2], nums[-1])
        for i in range(n-3, -1, -1):
            nums[i] = max((nums[i] + nums[i+2]), nums[i+1])       

        return nums[0]     

        
        