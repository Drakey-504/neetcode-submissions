class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        res = [0] * len(temp)

        stack = []

        for i in range(len(temp)):

            while stack and temp[stack[-1]] < temp[i]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)    

        return res            
        