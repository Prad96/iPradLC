class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict=defaultdict(int)
        for char in s:
                char_dict[char]+=1
        for key,value in char_dict.items():
            if value==1:
                return s.index(key)
        return -1