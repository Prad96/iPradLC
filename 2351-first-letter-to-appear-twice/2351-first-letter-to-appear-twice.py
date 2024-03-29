class Solution:
    def repeatedCharacter(self, s: str) -> str:
        character=dict()
        for char in s:
            if char not in character:
                character[char]=1
            else:
                return char