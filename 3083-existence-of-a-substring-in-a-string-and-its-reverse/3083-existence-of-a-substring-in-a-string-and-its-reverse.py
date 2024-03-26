class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for char in range(len(s)):
            substring=''
            for chars in range(char, len(s)):
                substring+=s[chars]
                if len(substring)==2 and substring in s[::-1]:
                    return True
        return False