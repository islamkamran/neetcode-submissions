class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            if second > first:
                heapq.heappush(max_heap, second-first)
        
        max_heap.append(0)
        return abs(max_heap[0])
