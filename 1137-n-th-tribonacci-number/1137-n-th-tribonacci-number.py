class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return n
        elif n == 1 or n == 2:
            return 1

        trib=[0]*(n+1)
        trib[0]=0
        trib[1]=1
        trib[2]=1
        for i in range(3,n+1):
            trib[i]=trib[i-3]+trib[i-2]+trib[i-1]
        return trib[n]