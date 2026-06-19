class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest_value = float('-inf')
        curr_value = 0
        for x in range(len(nums)):
            curr_value += nums[x]
            if nums[x] > curr_value:
                curr_value = nums[x]
            if curr_value > highest_value:
                highest_value = curr_value
        return highest_value