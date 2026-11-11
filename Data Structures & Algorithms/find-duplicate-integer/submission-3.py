class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow_p = 0
        fast_p = 0

        while True:

            slow_p = nums[slow_p]
            fast_p = nums[nums[fast_p]]

            if slow_p == fast_p:

                start_i = 0

                while start_i != slow_p:
                    start_i = nums[start_i]
                    slow_p = nums[slow_p]
                break

        return start_i       