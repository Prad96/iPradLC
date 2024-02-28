class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        final_sum=0
        if all(i<0 for i in nums):
            return max(nums)
        for i in nums:
            current_sum+=i
            if current_sum<0:
                current_sum=0
            if current_sum>final_sum:
                final_sum=current_sum
        return final_sum
        