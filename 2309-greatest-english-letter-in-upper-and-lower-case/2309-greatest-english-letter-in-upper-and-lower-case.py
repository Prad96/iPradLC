class Solution:
    def greatestLetter(self, s: str) -> str:
        s=sorted(set(s))[::-1]
        greatest_letter=''
        for letter in s:
            if letter.upper() in s and letter.lower() in s:
                return greatest_letter+letter.upper()
        return greatest_letter