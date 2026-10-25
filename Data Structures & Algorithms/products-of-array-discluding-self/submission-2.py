class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1] * len(nums)
        post = [1] * len(nums)
        front = 1
        back = 1
        j = len(nums) - 1

        for i in range(len(nums)):
            pre[i] *= front
            front *= nums[i]

            post[j] *= back
            back *= nums[j]
            j -= 1

        return [pre[i]*post[i] for i in range(len(nums))] 
         