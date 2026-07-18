class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if self.visited[node]:
                return
            self.remaining -= 1
            self.visited[node] = True
            for edge in self.connected[node]:
                dfs(edge)

        self.remaining = n
        self.connected = {}
        self.visited = {}
        for edge in edges:
            self.visited[edge[0]] = False
            self.visited[edge[1]] = False
            if edge[0] in self.connected:
                self.connected[edge[0]].append(edge[1])
            else:
                self.connected[edge[0]] = [edge[1]]

            if edge[1] in self.connected:
                self.connected[edge[1]].append(edge[0])
            else:
                self.connected[edge[1]] = [edge[0]]

        count = 0
        for node, is_visited in self.visited.items():
            if is_visited:
                continue
            count += 1
            dfs(node)

        return count + self.remaining
