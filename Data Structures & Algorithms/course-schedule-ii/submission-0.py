class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        adjacencies = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            inDegree[a] += 1
            adjacencies[b].append(a)

        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)
        
        taken = 0
        order = []
        while queue:
            course = queue.pop()
            taken += 1
            order.append(course)
            for prereq in adjacencies[course]:
                inDegree[prereq] -= 1
                if inDegree[prereq] == 0:
                    queue.append(prereq)

        return order if taken == numCourses else []