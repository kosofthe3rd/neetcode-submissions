class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = {i: [] for i in range(n)}
        visited = set()

        # Build an undirected graph
        for p, c in edges:
            tree[p].append(c)
            tree[c].append(p)

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in tree[node]:
                # Don't return through the edge we came from
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        # Check for a cycle
        if not dfs(0, -1):
            return False

        # Check that every node is connected
        return len(visited) == n