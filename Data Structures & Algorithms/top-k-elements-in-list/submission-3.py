class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        heap = []

        for key,val in freq.items():
            heapq.heappush(heap, (val,key)) 
            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]        