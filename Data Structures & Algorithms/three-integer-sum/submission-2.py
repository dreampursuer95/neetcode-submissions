class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans_set = set()
        visited = set()
        for i in range(0, len(nums)-2):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans_set.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        ans_list = []
        for ans in ans_set:
            ans_list.append(list(ans))
        return ans_list
