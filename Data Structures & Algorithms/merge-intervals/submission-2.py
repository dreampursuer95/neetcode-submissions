class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        ans = []

        min_val = sorted_intervals[0][0]
        max_val = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            if max_val >= sorted_intervals[i][0]:
                min_val = min(min_val, sorted_intervals[i][0])
                max_val = max(max_val, sorted_intervals[i][1])
            else:
                ans.append([min_val, max_val])
                min_val = sorted_intervals[i][0]
                max_val = sorted_intervals[i][1]
            if i == len(sorted_intervals) - 1:
                    ans.append([min_val, max_val])
        return ans
