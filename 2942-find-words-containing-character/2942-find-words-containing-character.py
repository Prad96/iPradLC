class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices=[]
        for word in range(len(words)):
            if x in words[word]:
                 indices.append(word)
        return indices