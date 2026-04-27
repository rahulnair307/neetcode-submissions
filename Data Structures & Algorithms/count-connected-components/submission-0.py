class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)] # root parent” (ultimate representative) of the set that n1 belongs to
        rank = [1] * n # size of the entire connected component

        # we want to find the nodes root parent
        def find(n1):
            res = n1
# we can stop searching once we have gotten to a node where the node itself is its own parent
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            # find the root parents of n1 and n2
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0 # indicate we did not perform a union
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1,n2) # -1 if successful or -0 if not successful
        return res