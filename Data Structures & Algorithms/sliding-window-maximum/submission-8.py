class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        res = []
        l = r = 0

        while r < k:
            heapq.heappush(heap,(-nums[r], r))
            r += 1
        res.append(-heap[0][0])  

        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))

            l += 1
            while heap and heap[0][1] < l:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            r += 1    

        return res   
