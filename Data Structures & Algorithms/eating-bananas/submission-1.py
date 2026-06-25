class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_num_of_hours(piles, k):
            h = 0
            for pile in piles:
                h += math.ceil(pile / k)
            return h
        
        max_num = 0
        for pile in piles:
            max_num = max(max_num, pile)
        start = 1
        end = max_num
        ans = 0
        while start <= end:
            mid = int((start + end) / 2)
            curr_h = get_num_of_hours(piles, mid)
            if curr_h > h:
                start = mid + 1
            else:
                end = mid - 1
                ans = mid
        return ans
