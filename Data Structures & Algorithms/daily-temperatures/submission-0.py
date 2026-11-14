class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        res = [0] * len(temp)

        stack = []

        for i in range(len(temp)):

            if stack and temp[stack[-1]] < temp[i]:

                while stack and temp[stack[-1]] < temp[i]:
                    prev_index = stack.pop()
                    res[prev_index] = i - prev_index
                    
                stack.append(i)    

            else:
                stack.append(i)

        while stack:
            prev_index = stack.pop()
            res[prev_index] = 0

        return res            
        