class Solution:
    def longestPalindrome(self, s: str) -> str:
        onlyPals=list()
        for char in range(len(s)):
            string=''
            for chars in range(char, len(s)):
                string+=s[chars]
                if string==string[::-1]:
                    onlyPals.append(string)
        return max(onlyPals,key=len)