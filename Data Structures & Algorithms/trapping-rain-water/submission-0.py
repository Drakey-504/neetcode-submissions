class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        l_g = [0] * n
        r_g = [0] * n


        for i in range(1, n):
            l_g[i] = max(height[i-1], l_g[i-1])

        for j in range(n-2, -1, -1):      
            r_g[j] = max(height[j+1], r_g[j+1])
        
        res = 0
        for i in range(n):
            tmp = min(l_g[i], r_g[i]) - height[i]
            if tmp < 0:
                tmp = 0
            res += tmp    

        return res    
