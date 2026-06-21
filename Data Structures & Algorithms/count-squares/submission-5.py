class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.pointsList = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.pointsList.append(point)

    def count(self, point: List[int]) -> int:
        c = 0
        for p in self.pointsList:
            if point[0] == p[0] and point[1] == p[1]:
                continue
            if abs(point[0]-p[0]) == abs(point[1]-p[1]):
                if self.pointsCount[(point[0], p[1])] > 0 and self.pointsCount[(p[0], point[1])] > 0:
                    c += self.pointsCount[(point[0], p[1])] * self.pointsCount[(p[0], point[1])]
        return c
