class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_counts=0
        for word in words:
            if word[0:len(pref)]==pref:
                prefix_counts+=1
        return prefix_counts