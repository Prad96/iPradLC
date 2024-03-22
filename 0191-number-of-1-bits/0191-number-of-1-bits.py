class Solution:
    def hammingWeight(self, n: int) -> int:
        if n>2147483647:
            return "'n' to have value from 0 to 2147483647 only"
        return bin(n).count('1')
    