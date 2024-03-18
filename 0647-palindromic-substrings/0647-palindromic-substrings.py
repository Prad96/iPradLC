class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_substrings=list()
        for i in range(len(s)):
            substring=''
            for j in range(i,len(s)):
                substring+=s[j]
                if substring==substring[::-1]:
                    palindrome_substrings.append(substring)
        return len(palindrome_substrings)
