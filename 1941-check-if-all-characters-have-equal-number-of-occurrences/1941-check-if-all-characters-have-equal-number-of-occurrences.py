class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if len(set(s))==1:
            return True
        characters=dict()
        for char in s:
            characters[char]=characters.get(char,0)+1
        return len(set(characters.values()))==1