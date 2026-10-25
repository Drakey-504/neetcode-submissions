class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)
        res = 0

        for n in nums:
            if (n-1) not in hash_set:
                cur_seq = 1
                temp = n
                while (temp+1) in hash_set:
                    cur_seq += 1
                    temp += 1

                if res < cur_seq:
                    res = cur_seq       

        return res
        