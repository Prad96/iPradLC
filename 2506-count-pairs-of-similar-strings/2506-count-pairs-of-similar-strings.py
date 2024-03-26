class Solution:
    def similarPairs(self, words: List[str]) -> int:
        similar_pairs=0
        for word in range(len(words)):
            for next_word in range(word+1, len(words)):
                if sorted(set(words[word]))==sorted(set(words[next_word])):
                    similar_pairs+=1
        return similar_pairs