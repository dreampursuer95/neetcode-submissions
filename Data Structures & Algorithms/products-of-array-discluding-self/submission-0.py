class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pa = [0] * n
        sa = [0] * n
        ra = [0] * n
        pa[0] = sa[n - 1] = 1
        for i in range(1, n):
            pa[i] = pa[i - 1] * nums[i - 1]
            sa[n - 1 - i] = sa[n - i] * nums[n - i]
        for i in range(n):
            ra[i] = pa[i] * sa[i]
        return ra
