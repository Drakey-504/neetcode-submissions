class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:

            while l <= r:
                m = l + (r-l)//2

                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m + 1           
            return -1        

        while l < r: 
            m = l + (r-l)//2

            if nums[l] < nums[m]:
                l = m
            else:
                r = m 

        def_ind = l

        if target <= nums[def_ind] and target >= nums[0]:
            l, r = 0, def_ind
        else:
            l, r = def_ind+1, len(nums) - 1

        while l <= r:
                m = l + (r-l)//2

                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m + 1           
        return -1     

