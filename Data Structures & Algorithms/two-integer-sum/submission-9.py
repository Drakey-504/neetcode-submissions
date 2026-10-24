class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h_map = {}

        for i,n in enumerate(nums):
            if n in h_map:
                return [h_map[n], i]
            else:
                h_map[target-n] = i

        return None        

        