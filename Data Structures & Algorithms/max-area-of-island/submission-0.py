class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get the AREA of an island -> DFS
        # then return the maximum area

        row = len(grid)
        col = len(grid[0])
        visitedSet = set()
        maxArea = 0

        def dfs(r,c):
            if (r not in range(row) or c not in range(col) or (r,c) in visitedSet or grid[r][c] == 0):
                return 0    # 0 area because no island so return area
            
            visitedSet.add((r,c))

            # each of these dfs calc area and the one cell we are currently visiting right now
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))


        for r in range(row):
            for c in range(col):
                if (grid[r][c] == 1 and (r,c) not in visitedSet):
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea