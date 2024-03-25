class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority=set()
        for num in nums:
            if nums.count(num)>(len(nums)//3):
                majority.add(num)
        return majority