class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], [nums[0]]]
        prev_subsets = self.subsets(nums[:len(nums)-1])
        res = prev_subsets.copy()
        for subset in prev_subsets:
            subset_copy = subset.copy()
            subset_copy.append(nums[len(nums)-1])
            res.append(subset_copy)
        return res
