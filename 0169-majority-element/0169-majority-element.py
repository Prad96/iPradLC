# from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return max(Counter(nums),key=Counter(nums).get)
    
        nums_dict=defaultdict(int)
        n = len(nums) // 2
        for i in nums:
                nums_dict[i]+=1
                
        for key,value in nums_dict.items():
            if value>n:
                return key
                    
            
            
