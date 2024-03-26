class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenCount=0
        for num in nums:
            num=str(num)
            number_length=len(num)
            if number_length%2==0:
                evenCount+=1
        return evenCount