class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i, target):
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            if (i, target) in dp:
                return dp[(i, target)]
            dp[(i, target)] = backtrack(i+1, target-nums[i]) + backtrack(i+1, target+nums[i])
            return dp[(i, target)]

        return backtrack(0, target)

        