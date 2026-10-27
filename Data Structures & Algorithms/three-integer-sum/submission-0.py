class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()
        arr_len = len(nums)

        for k in range(arr_len-2):
            i, j = k+1, arr_len - 1
            while i < j:
                cur_sum = nums[i] + nums[j]

                if cur_sum < -nums[k]:
                    i += 1
                elif cur_sum > -nums[k]:
                    j -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    i += 1        

        return list(res)