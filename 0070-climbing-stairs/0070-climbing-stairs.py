class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        ways=[0]*n
        ways[0]=1
        ways[1]=2
        for i in range(2,n):
            ways[i]=ways[i-2]+ways[i-1]
        print(ways)
        return ways[n-1]
                           