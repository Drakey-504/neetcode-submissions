class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        dp_cache = [-1] * n

        def maxMoneyFromIndex(i, mod_array):

            if i >= len(mod_array):
                return 0

            if dp_cache[i] == -1:
                dp_cache[i] = max(mod_array[i] + maxMoneyFromIndex((i+2),mod_array), maxMoneyFromIndex((i+1), mod_array))

            return dp_cache[i]

        with_start = nums[1:]
        with_start_res = maxMoneyFromIndex(0, with_start)

        dp_cache = [-1] * n
        without_start = nums[:n-1]
        without_start_res = maxMoneyFromIndex(0, without_start)

        return max(with_start_res, without_start_res)