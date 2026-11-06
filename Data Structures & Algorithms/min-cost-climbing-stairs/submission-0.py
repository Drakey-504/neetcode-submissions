class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp_cache = [-1] * (len(cost) + 1)


        def minCost(i) -> int:

            if i < 2:
                dp_cache[i] = 0

            if dp_cache[i] == -1:  
                dp_cache[i] = min((minCost(i-1) + cost[i-1]), (minCost(i-2) + cost[i-2]))
            
            return dp_cache[i]

        return minCost(len(cost))   