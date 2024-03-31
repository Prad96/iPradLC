class Solution:
    def greatestLetter(self, s: str) -> str:
        greatest_letter=''
        for letter in s:
            uppercase,lowercase=letter.upper(), letter.lower()
            if uppercase in s and lowercase in s:
                greatest_letter+=letter
        return max(greatest_letter.upper(), default='')