class Solution:
    def pivotInteger(self, n: int) -> int:
        left=1
        right=n
        leftsum=left
        rightsum=right
        if n==1:
            return 1
        while(left<right):
            if(leftsum<rightsum):
                left+=1
                leftsum+=left
            else:
                right-=1
                rightsum+=right
                
        if leftsum==rightsum and left==right:
            return left
        else:
            return -1