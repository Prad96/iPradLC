class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substring_count=0
        for pattern in patterns:
            if pattern in word:
                substring_count+=1
        return substring_count
                