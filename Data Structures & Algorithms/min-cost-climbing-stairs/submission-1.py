class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp_cache = [-1] * (len(cost) + 1)
        dp_cache[0] = 0
        dp_cache[1] = 0

        for i in range(2,len(cost)+1):
            dp_cache[i] = min((dp_cache[i-1]+cost[i-1], dp_cache[i-2] + cost[i-2]))

        return dp_cache[-1]    
        