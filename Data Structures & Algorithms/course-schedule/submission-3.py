class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adj list map Course to their prerequistes
        # i need to go through every course and check their prereq and i cannot have a loop
            # my graph needs to be acyclic graph
        # topological sort problem and my graph has directed edges
        mapPrereq = {}
        for i in range(numCourses):
            mapPrereq[i] = []
        
        for course, prereq in prerequisites:
            mapPrereq[course].append(prereq)
        
        # keep track of courses in current DFS path remove after path
        visit = set()

        def dfs(currCourse):
            if currCourse in visit:
                return False
            if mapPrereq[currCourse] == []:  # i have already processed this currcourse
                return True
            
            visit.add(currCourse)

            for preCourse in mapPrereq[currCourse]:
                if (dfs(preCourse) == False):
                    return False
            visit.remove(currCourse)
            mapPrereq[currCourse] = [] # i am done processing this course because i went through all the neighbors and did not have any problem
            
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True