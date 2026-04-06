class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        if no cycles, valid tree
        every node must be connected to something
        if n == visited nodes, return True
        """

# adjacency list
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for nei_node in graph[node]:
                if nei_node == prev:
                    continue
                if not dfs(nei_node, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n