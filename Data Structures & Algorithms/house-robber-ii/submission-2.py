class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        mem = dict()

        def get_max_rob(i, last_house_taken):
            if (i,last_house_taken) in mem:
                return mem[(i,last_house_taken)]

            if i < 0:
                return 0
            if i == 0:
                if last_house_taken:
                    return 0
                else:
                    return nums[i]

            mem[(i,last_house_taken)] = max(get_max_rob(i-2, last_house_taken) + nums[i], get_max_rob(i-1, last_house_taken))
            return mem[(i,last_house_taken)]

        return max(get_max_rob(len(nums)-1, True), get_max_rob(len(nums)-2, False))