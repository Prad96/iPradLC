class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_dict={}
        for i in nums:
            if i not in single_dict:
                single_dict[i]=1
            else:
                single_dict[i]+=1
        for key,value in single_dict.items():
            if value == 1:
                return key
        