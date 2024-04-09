class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings= list()
        for substring in words:
            for string in words:
                if substring!=string and substring in string:
                    substrings.append(substring)
                    break
        return substrings