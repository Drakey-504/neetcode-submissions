class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        
        for n in nums:
            freq_map[n] = 1 + freq_map.get(n,0)

        heap_q = []

        heapq.heapify(heap_q)

        for key,val in freq_map.items():
            heapq.heappush(heap_q, (-val,key))

        res = []
        
        for i in range(k):
            res.append(heapq.heappop(heap_q)[1])

        return res    

