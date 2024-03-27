class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pairs=0
        distinct=set()
        for word in words:
            if word in distinct or word[::-1] in distinct:
                pairs+=1
            else:
                distinct.add(word)
        return pairs