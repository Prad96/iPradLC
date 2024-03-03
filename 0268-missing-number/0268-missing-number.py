class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum=((len(nums) * (len(nums)+1)))/2
        missing_sum=sum(nums)
        return int(actual_sum-missing_sum)