class Solution:
    def countBits(self, n: int) -> List[int]:
        ones=list()
        for i in range(n+1):
            ones.append(bin(i).count('1'))
        return ones