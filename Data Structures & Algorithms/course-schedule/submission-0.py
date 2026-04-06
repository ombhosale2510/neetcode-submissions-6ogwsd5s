class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahs algo
        # keep reducing incoming-=1 after initial nodes, 
        # so that every prereq is taken care of, count+=1
        # if by the end we have done all prereq, count==numCourses, True

        indegree = defaultdict(int)
        graph = defaultdict(list)

        for src, dst in prerequisites:
            indegree[dst]+=1
            graph[src].append(dst)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        result= 0
        while q:
            node = q.popleft()
            result+=1
            
            for nei_node in graph[node]:
                indegree[nei_node]-=1
                if indegree[nei_node] == 0:
                    q.append(nei_node)
        
        return result==numCourses






