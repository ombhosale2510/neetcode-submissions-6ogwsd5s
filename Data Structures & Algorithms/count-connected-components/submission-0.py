class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        total n of connected components
        count how many nodes are connected to each other
        for every node, do dfs to find nei_nodes and put them in visited set
        and increment when a connected component (group) is found or formed
        """

        graph = defaultdict(list)

        count = 0 

        visited = set()

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        # graph traversal

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei_node in graph[node]:
                dfs(nei_node)

        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1
        return count

