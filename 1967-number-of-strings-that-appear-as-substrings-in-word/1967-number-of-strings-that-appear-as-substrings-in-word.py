class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        substrings_word,count=[],0
        for char in range(len(word)):
            substring=''
            for string in range(char, len(word)):
                substring+=word[string]
                substrings_word.append(substring)
        for pattern in patterns:
            if pattern in substrings_word:
                count+=1
        return count
                