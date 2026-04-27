import heapq
class Solution:
    '''
    - since I want the kth largest element in the array what i can do is when keep poping out 
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # TC: O(N+klgN)
        # # using MaxHeap and popping k times to get the largest k element

        # for i in range(len(nums)):
        #     nums[i] = -(nums[i])
        
        # heapq.heapify(nums) # in-place act as a maxheap

        # for _ in range(k-1):    # remember actually going from 0 up to (k-2)
        #     heapq.heappop(nums)
        
        # return -(heapq.heappop(nums))   # negate it back to make positive

        # using MinHeap but building as you go
        # TC: O(Nlgk)
        # SC: O(k)
        heap = []

        for i in nums:
            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
