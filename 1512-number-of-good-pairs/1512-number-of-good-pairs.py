class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i,goodPairs,j=0,0,len(nums)-1
        while i<j:
            if nums[i]==nums[j]:
                goodPairs+=1
                j-=1
            else:
                j-=1                                                                                                           
            if i==j:
                i+=1
                j=len(nums)-1 
        return goodPairs
             
