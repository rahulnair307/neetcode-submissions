class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    # ### BFS Solution
    #     if not grid:
    #         return 0

    #     row = len(grid)
    #     col = len(grid[0])
    #     visitedSet = set()
    #     islandCounter = 0

    #     def bfs(r, c):
    #         q = deque()
    #         visitedSet.add((r,c))
    #         q.append((r,c))

    #         while q:
    #             r1, c1 = q.popleft()
    #             directions = [[1,0], [-1,0], [0, 1], [0,-1]] 
    #             for i, j in directions:
    #                 newR = r1 + i
    #                 newC = c1 + j

    #                 if (newR in range(row) and newC in range(col) and (newR, newC) not in visitedSet and grid[newR][newC] == "1"):
    #                     visitedSet.add((newR, newC))
    #                     q.append((newR, newC))
            


    #     for r in range(row):
    #         for c in range(col):
    #             if grid[r][c] == "1" and (r, c) not in visitedSet:
    #                 bfs(r, c)
    #                 islandCounter += 1
        
    #     return islandCounter
    
    ### Recursive DFS
        if not grid:
            return 0
        #dimensions
        row = len(grid)
        col = len(grid[0])
        visitedSet = set()  # tuple coordinate (r, c)
        islandCounter = 0

        def dfs(r, c):
            if (r not in range(row) or c not in range(col) or grid[r][c] != "1" or (r,c) in visitedSet):
                return

            visitedSet.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visitedSet:
                    dfs(r, c)
                    islandCounter += 1
        
        return islandCounter