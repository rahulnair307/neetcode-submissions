class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # weight of the edge is the time it takes to go from source to target
        # k is the starting point
        # dijkstra -> BFS (layer by layer) and MinHeap (every time we want to get minimum from minheap it is (logn) operation)

        # create adjacency list
        edgesMap = {}
        for i in range(1,n+1):
            edgesMap[i] = []
        for u,v,w in times:
            edgesMap[u].append((v,w))
        
        # create minheap
        minHeap = [(0, k)] # (time so far, starting)
        visit = set()
        maxTime = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            maxTime = max(maxTime, w1)

            #BFS go through the neighbors
            for n2, w2 in edgesMap[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))

        if len(visit) == n:
            return maxTime
        return -1