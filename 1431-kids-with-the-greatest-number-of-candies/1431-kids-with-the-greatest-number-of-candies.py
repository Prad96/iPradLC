class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        booleans=list()
        for candy in candies:
            booleans.append(candy+extraCandies>=max(candies))
        return booleans