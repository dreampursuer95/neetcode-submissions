class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.kthLargest = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.kthLargest:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.kthLargest:
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) >= self.kthLargest and self.min_heap[0] < val:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]

        
