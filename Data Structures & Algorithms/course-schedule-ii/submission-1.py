class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # same as course schedule 1, literally only kahns algorithm

        indegree = defaultdict(int)
        # adjacency list
        graph = defaultdict(list)

        for src, dst in prerequisites:
            indegree[dst]+=1
            graph[src].append(dst)

        q = deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)

        result = []
        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            result.append(node)

            for nei_node in graph[node]:
                indegree[nei_node]-=1
                if indegree[nei_node]==0:
                    q.append(nei_node)
        
        if finish!= numCourses:
            return []
                    
        return result[::-1]