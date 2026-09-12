class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPrereqs = [0] * numCourses
        adjacencies = [[] for crs in range(numCourses)]

        for crs, pre in prerequisites:
            numPrereqs[crs] += 1
            adjacencies[pre].append(crs)
        
        queue = []
        for crs in range(numCourses):
            if numPrereqs[crs] == 0:
                queue.append(crs)

        taken = 0
        while queue:
            crs = queue.pop()
            taken += 1
            for dep in adjacencies[crs]:
                numPrereqs[dep] -= 1
                if numPrereqs[dep] == 0:
                    queue.append(dep)

        return True if taken == numCourses else False
