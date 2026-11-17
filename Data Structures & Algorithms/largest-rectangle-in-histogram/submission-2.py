class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)

        stack = []
        res = 0

        for i in range(0, len(heights)):
            
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)             

        stack = []

        for i in range(len(heights)-1, -1 ,-1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]     

            stack.append(i)     

        for i in range(0, len(heights)):
            left[i] += 1
            right[i] -= 1
            cur_area = heights[i] * (right[i] - left[i] + 1)
            res = max(res,cur_area)

        return res