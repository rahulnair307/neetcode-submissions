class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pair [0, 1]
        # use adjacency list hashmap
        # - for each of our courses will map prereq
        # run dfs on course and then its neighbor and check if we can COMPLETE THE COURSE
        # empty prereq list means it can be completed
        # if every prereq list is empty than we can return true

        # how to know there is a cycle
            # create a visit hashset while we run dfs
            # if we go to node that is in visitset then we have to return false
        preMap = {}
        # create empty list of prereq for each course
        for i in range(numCourses): 
            preMap[i] = []
            # fill out the prereq adjacency list
        for course,prereq in prerequisites:
            preMap[course].append(prereq) # you dont want to overwrite u want to append to create new
        
        #visitSet tracks nodes on the current DFS path (not all visited ever—just the active recursion chain).
        visitSet = set()

        def dfs(currCourse):
            if currCourse in visitSet:  # detect cycle
                return False
            if preMap[currCourse] == []:
                return True
            
            # process node
            visitSet.add(currCourse)

            for pre in preMap[currCourse]:  #neighbors
                if dfs(pre) == False:
                    return False
            visitSet.remove(currCourse)
            preMap[currCourse] = [] # I’ve confirmed currCourse is finishable; from now on, treat it as having no remaining prerequisites
            return True
        
        # run dfs on every single node and if any course cant be finished that its cooked
        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True