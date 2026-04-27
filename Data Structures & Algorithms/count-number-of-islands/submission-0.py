class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    ### Recursive DFS
        if not grid:
            return 0
        #dimensions
        row = len(grid)
        col = len(grid[0])
        visitedSet = set()  # tuple coordinate (r, c)
        islandCounter = 0

        def dfs(r, c):
            if (r >= row or c >= col or c < 0 or r < 0 or grid[r][c] != "1" or (r,c) in visitedSet):
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





