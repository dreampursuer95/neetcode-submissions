class Solution:
    hm = dict()
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        if n in self.hm:
            return self.hm[n]
        
        self.hm[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.hm[n]
