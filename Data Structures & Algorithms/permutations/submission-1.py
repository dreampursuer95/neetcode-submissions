class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perms, nums, picked):
        if len(perms) == len(nums):
            self.res.append(perms[:])
            return

        for i in range(len(nums)):
            if not picked[i]:
                perms.append(nums[i])
                picked[i] = True
                self.backtrack(perms, nums, picked)
                perms.pop()
                picked[i] = False