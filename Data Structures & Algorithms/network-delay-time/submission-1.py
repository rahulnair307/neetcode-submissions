class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # weight of the edge is the time it takes to go from source to target
        # k is the starting point
        # dijkstra -> BFS (layer by layer) and MinHeap (every time we want to get minimum from minheap it is (logn) operation)

        # create my adjcency list [source, (target, time)]
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for u,v,t in times:
            adj[u].append((v,t))
        
        # create my minHeap
        minHeap = [(0, k)] # (time so far, startnode)
        visit = set()
        maxTime = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            maxTime = max(maxTime, t1)  # doubt here

            for n2, t2 in adj[n1]:
                if n2 not in visit:     # doubt in this area
                    heapq.heappush(minHeap, (t1+t2, n2))
            
        if len(visit) == n:
            return maxTime
        return -1