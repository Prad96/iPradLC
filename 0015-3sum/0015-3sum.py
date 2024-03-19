class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        # print(nums)
        three_sum_list=set()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                
                if nums[i]+nums[left]==-nums[right]:
                    # if [nums[i], nums[left], nums[right]] not in three_sum_list:
                    three_sum_list.add((nums[i],nums[left],nums[right]))
                    # print(three_sum_list)
                    left+=1
        
                elif nums[i]+nums[left]<-nums[right]:
                    left+=1
                    
                else:
                    right-=1
                # return three_sum_list
        return list(three_sum_list)
                
                