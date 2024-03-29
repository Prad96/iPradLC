class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        character_index=word.index(ch)
        prefix=word[:character_index+1]
        suffix=word[character_index+1:]
        return prefix[::-1]+suffix