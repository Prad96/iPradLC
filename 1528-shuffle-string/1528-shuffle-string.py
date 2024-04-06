class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffledString=['']*len(s)
        for char,index in zip(s, indices):
            shuffledString[index]=char
        return ''.join(shuffledString)