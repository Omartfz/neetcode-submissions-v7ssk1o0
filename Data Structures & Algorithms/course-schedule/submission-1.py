class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist={i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adjlist[a].append(b)
        visit=set()
        def dfs(node):
            if node in visit:
                return False
            if adjlist[node]==[]:
                return True
            visit.add(node)
            for nei in adjlist[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            
            return True
        for node in range(numCourses):
            if not dfs(node):
                return False
        return True








        

        