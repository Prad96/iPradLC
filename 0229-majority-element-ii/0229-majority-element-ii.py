class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority=set()
        nums_dict=defaultdict(int)
        for num in nums:
            nums_dict[num]=nums_dict.get(num,0)+1
        for key,value in nums_dict.items():
            if value>(len(nums)//3):
                majority.add(key)
        return list(majority)