# https://leetcode-cn.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2 = 1, 2
        for i in range(3, n+1):
            f3 = f1 + f2
            f1, f2 = f2, f3
        return f3
