class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [0] * len(nums)
        def get_lis(i):
            if mem[i]:
                return mem[i]
            max_length = 1
            for j in range (i-1, -1, -1):
                lis_j = get_lis(j)
                if nums[i] > nums[j]:
                    max_length = max(max_length, lis_j+1)
            mem[i] = max_length
            return mem[i]
        return max(get_lis(i) for i in range (len(nums)-1, -1, -1))
