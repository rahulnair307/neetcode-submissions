class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # water can flow if neighboring cell's height is <= current height
        # can flow in only 4 directions
        # brute force would be to go to every (r,c) and do dfs or bfs to see the 4 neighboring and see if it will reach from pacific to atlantic but that would be O(m*n)^2

        # optimized solution: 
        # - you will start from the heights that boarder the ocean so lets say we start from pacific ocean we take those boardering heights and run DFS to see what heights the water will flow til. we also do this for atlantic ocean heights and respecitvelly append to the set and then in the end our result are the heights or the coordincates (r,c) where both atlantic and pacific have been crossed
        # instead of going and checking less than or equal since we are going from the other side we need to check greater than or equal to
        # have a visit set so we do not count duplicates

        rows = len(heights)
        cols = len(heights[0])

        pac = set() # visited set store tuples (r,c)
        atl = set() # visited set

        def dfs(r, c, visitSet, prev):
            if ((r,c) in visitSet or r not in range(rows) or c not in range(cols) or heights[r][c] < prev):
                return
            
            visitSet.add((r,c))

            dfs(r+1, c, visitSet, heights[r][c])
            dfs(r-1, c, visitSet, heights[r][c])
            dfs(r, c+1, visitSet, heights[r][c])
            dfs(r, c-1, visitSet, heights[r][c])

        # starting the dfs from boardering heights in atl and pac
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) #pac
            dfs(rows-1, c, atl, heights[rows-1][c]) #atl
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # pac
            dfs(r, cols - 1, atl, heights[r][cols-1]) # atl
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result

# TC: O(m*n)