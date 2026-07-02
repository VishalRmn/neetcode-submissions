import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}

        for n in nums:
            my_map[n] = 1 + my_map.get(n, 0)

        max_heap = [(-value, key) for (key, value) in my_map.items()]
        heapq.heapify(max_heap)

        top_k_keys = []
        for _ in range(min(k, len(max_heap))):
            neg_value, key = heapq.heappop(max_heap)
            top_k_keys.append(key)

        return top_k_keys

        
        