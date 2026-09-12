class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # numPrereqs = [0] * numCourses
        # preMap = [[] for crs in range(numCourses)]

        # for crs, pre in prerequisites:
        #     numPrereqs[crs] += 1
        #     preMap[pre].append(crs)

        # queue = []
        # for crs in range(numCourses):
        #     if numPrereqs[crs] == 0:
        #         queue.append(crs)

        # taken = 0
        # order = []

        # while queue:
        #     crs = queue.pop()
        #     taken += 1
        #     order.append(crs)
        #     for dep in preMap[crs]:
        #         numPrereqs[dep] -= 1
        #         if numPrereqs[dep] == 0:
        #             queue.append(dep)

        
        # return order if taken == numCourses else []

        preMap = [[] for crs in range(numCourses)]
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        curPath, visited = set(), set()
        order = []
        def dfs(crs):
            if crs in curPath:
                return False
            
            if crs in visited:
                return True

            curPath.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            curPath.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return order
