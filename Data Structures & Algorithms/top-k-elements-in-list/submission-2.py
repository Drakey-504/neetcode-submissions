class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        groups = defaultdict(int)

        for n in nums:
            groups[n] += 1

        heap_bkt = []

        for key,val in groups.items():
            heap_bkt.append((-val, key))
        
        heapq.heapify(heap_bkt)   

        res = []

        for i in range (k):
            res.append(heapq.heappop(heap_bkt)[1]) 

        return res    