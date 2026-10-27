class Solution:
    def maxArea(self, heights: List[int]) -> int:

        if len(heights) == 0 or len(heights) == 1:
            return 0 

        l, r, res = 0, len(heights) - 1 ,0

        while l < r:

            cur_area = min(heights[l], heights[r]) * (r-l)
            
            if res < cur_area:
                res = cur_area

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res            
        