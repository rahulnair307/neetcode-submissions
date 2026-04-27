import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ### REMEMBER HEAPQ WORKS ON MINHEAP NOT MAXHEAP
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            secondLargest = heapq.heappop(stones)

            if largest < secondLargest:
                diff = largest - secondLargest
                heapq.heappush(stones, diff)
        
        if stones:
            return -stones[0]
        else:
            return 0