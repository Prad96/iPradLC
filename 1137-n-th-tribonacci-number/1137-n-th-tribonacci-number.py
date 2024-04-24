class Solution:
    def tribonacci(self, n: int) -> int: 
        if n==0:
            return 0
        elif n>0 and n<3:
            return 1
        tribonacci_numbers=[0]*(n+1)
        tribonacci_numbers[0]=0
        tribonacci_numbers[1]=1
        tribonacci_numbers[2]=1
        for num in range(3,n+1):
            tribonacci_numbers[num]=tribonacci_numbers[num-3]+tribonacci_numbers[num-2]+tribonacci_numbers[num-1]
        
        ''''t[3]=2
        [0,1,1,2,0,0,0]
        [0,1,1,2,4,0,0]
        [0,1,1,2,4,7,0]
        [0,1,1,2,4,7,13]'''
        
        return tribonacci_numbers[num]