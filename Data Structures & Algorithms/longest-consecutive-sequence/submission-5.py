class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        res = 0

        for n in nums:

            if n-1 not in num_set:
                cur_len = 0
                cur_n = n
                while cur_n in num_set:
                    cur_len += 1
                    cur_n += 1
                res = max(res, cur_len)    

        return res
