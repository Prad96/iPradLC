class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left,right,balanced=0,0,0
        for char in s:
            if char=='L':
                left+=1
            if char=='R':
                right+=1
            if left==right:
                balanced+=1
        return balanced
        