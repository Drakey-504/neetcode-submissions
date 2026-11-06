class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)

        def maxMoneyFromIndex(i):

            if i >= len(nums):
                return 0

            if dp[i] == -1:
                dp[i] = max (nums[i] + maxMoneyFromIndex(i+2), maxMoneyFromIndex(i+1))

            return dp[i]  

        return maxMoneyFromIndex(0)         

        