class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # MAIN IDEA: trees cannot have loops and a tree needs to be connected
        # using these edges we want to make an adjacency list
        # empty graph counts as tree
        # 1)TO CHECK FOR CONNECTED
        # for every single node visit neighbors recursivly 
            # if the number of visited nodes matches the input value for nodes then it is connected
        #2) TO CHECK FOR LOOP IN undirected
        # edge case is that everytime we go to neighbor since it is a undirected edge we will go back and think there is a loop
            # USE A PREVIOUS so we know we cant go back that same way (default to -1 when we pass in)

        if not n:
            return True

        visit = set()
        adj = {}
        for i in range(n):
            adj[i] = []

        # since it is undirected remember to show relationship both ways
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

    
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node) == False: # loop detected
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)