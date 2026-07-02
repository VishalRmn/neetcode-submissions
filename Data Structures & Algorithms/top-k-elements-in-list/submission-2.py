class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = {}
        for num in nums:
            counter_nums[num] = 1 + counter_nums.get(num, 0)
        
    
        heap = []
        for key in counter_nums.keys():
            heapq.heappush(heap, [counter_nums[key], key])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        