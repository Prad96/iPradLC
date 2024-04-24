class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        longest_length=0
        for char in range(len(s)):
            substring=''
            for chars in range(char, len(s)):
                substring+=s[chars]
                length=len(substring)
                if  length==len(set(substring)):
                    longest_length=max(length,longest_length)
                else:
                    break
        return longest_length