class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(point1, point2):
            return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

        adj = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = get_dist(points[i], points[j])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        h = [[0,0]]
        visited = set()
        cost = 0
        while len(visited) < len(points):
            least_dist, index = heapq.heappop(h)
            if index in visited:
                continue
            cost += least_dist
            visited.add(index)
            for nei_cost, nei in adj[index]:
                 heapq.heappush(h, [nei_cost, nei])

        return cost

