class Solution:
    def scoreOfString(self, s: str) -> int:
        string_score=0
        for char in range(1,len(list(s))):
            string_score+=abs(ord(s[char-1])-ord(s[char]))
        return string_score