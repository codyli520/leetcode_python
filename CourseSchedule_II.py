class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if not prerequisites or len(prerequisites) == 0:
            return [n for n in range(numCourses)]
        
        indegree = [0 for n in range(numCourses)]
        dependent_courses = collections.defaultdict(list)
        
        for pair in prerequisites:
            indegree[pair[0]] += 1
            dependent_courses[pair[1]].append(pair[0])
        
        result = []
        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            course = queue.popleft()
            result.append(course)
            for subcourse in dependent_courses[course]:
                indegree[subcourse] -= 1
                if indegree[subcourse] == 0:
                    queue.append(subcourse)
        
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return []
        
        return result