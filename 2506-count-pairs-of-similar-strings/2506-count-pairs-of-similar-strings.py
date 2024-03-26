class Solution:
    def similarPairs(self, words: List[str]) -> int:
        similar=dict()
        similar_pairs=0
        for word in words:
            word=''.join(sorted(set(word)))
            similar[word]=similar.setdefault(word,0)+1
        for key,value in similar.items():
            similar_pairs+=(value)*(value-1)//2
        return similar_pairs