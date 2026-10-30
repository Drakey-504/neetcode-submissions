class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) < k:
            return []

        res = []
        max_heap = []
        l=0

        heapq.heapify(max_heap)

        for r in range(k):
            heapq.heappush(max_heap, (-nums[r], r))

        res.append(-max_heap[0][0])

        for r in range(k,len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            
            l += 1 

            while max_heap[0][1] < l:
                heapq.heappop(max_heap)   

            res.append(-max_heap[0][0])

        return res