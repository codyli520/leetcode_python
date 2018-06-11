class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 如果没有prereq， 直接return True
        if not prerequisites or len(prerequisites) == 0 :
            return True
        
        indegree = [0 for n in range(numCourses)] # course's indegree
        dependent_courses = collections.defaultdict(list) # course: list of courses that requires it
        
        # 记录每个course的indegree和它的prereqs
        for pair in prerequisites:
            indegree[pair[0]] += 1
            dependent_courses[pair[1]].append(pair[0])
    
        # BFS
        queue = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            
            for subcourse in dependent_courses[course]:
                # 如果有cycle，这里indegree会变负数，并且不会再被加到queue
                indegree[subcourse] -= 1
                if indegree[subcourse] == 0:
                    queue.append(subcourse)
                    
        # 如果有cycle，indegree会不等于0
        for n in indegree:
            if n != 0:
                return False
        
        return True