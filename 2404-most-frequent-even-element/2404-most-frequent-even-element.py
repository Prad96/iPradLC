class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        frequent=dict()
        max_even=0
        most_frequent=-1
        for num in nums:
            if num%2==0:
                frequent[num]=frequent.setdefault(num,0)+1
        for key,value in frequent.items():
            if value>max_even:
                max_even=value
                most_frequent=key
            elif value==max_even:
                most_frequent=min(key,most_frequent)
        return most_frequent
   