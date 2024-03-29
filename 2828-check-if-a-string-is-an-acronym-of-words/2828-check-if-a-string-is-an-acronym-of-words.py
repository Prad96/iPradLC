class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym=True
        initials=''
        if len(words)!=len(s):
            return not acronym
        for word in words:
            initials+=word[0]
        if initials==s:
            return acronym