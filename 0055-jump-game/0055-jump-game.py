class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hop=0
        for num in nums:
            if hop<0:
                return False
            elif num>hop:
                hop=num
                hop-=1
            else:
                hop-=1
        return True
    