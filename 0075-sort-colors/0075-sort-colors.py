class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        
        Do not return anything, modify nums in-place instead.
        """
        zerocount,onecount,twocount=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                zerocount+=1
            elif nums[i]==1:
                onecount+=1
            else:
                twocount+=1
        loop_var=0
        while zerocount>0:
            nums[loop_var]=0
            loop_var+=1
            zerocount-=1
        while onecount>0:
            nums[loop_var]=1
            loop_var+=1
            onecount-=1
        while twocount>0:
            nums[loop_var]=2
            loop_var+=1
            twocount-=1