class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_dict={}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num]=1
            else:
                nums_dict[num]+=1
        # print(nums_dict)
        values=list(nums_dict.values())
        # print(values)
        # total=0
        max_val=max(values)
        max_freq_list=[]
        for value in values:
            if value==max_val:
                max_freq_list.append(value)
        return sum(max_freq_list)
    
    