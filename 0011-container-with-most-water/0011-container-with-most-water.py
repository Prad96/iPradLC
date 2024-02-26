class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_amount_water=0
        while left < right:
            distance=right-left
            can_contain=min(height[left],height[right])
            area=distance*can_contain
            if area>max_amount_water:
                max_amount_water=area
            elif height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_amount_water