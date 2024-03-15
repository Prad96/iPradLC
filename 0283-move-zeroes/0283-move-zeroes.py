class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        # left=0
        # right=len(nums)-1
        # while left<right:
        #       if nums[right] == 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right -= 1
        #       else:
        #         left += 1
        
        
        
        zero_count=nums.count(0)
        for i in range(zero_count):
            nums.remove(0)
        nums+=[0]*zero_count