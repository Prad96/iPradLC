class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict={}
        for string in strs:
            sorted_string=''.join(sorted(string))
            if sorted_string not in anagram_dict:
                anagram_dict[sorted_string]=[string]
                # print(anagram_dict)
            else:
                anagram_dict[sorted_string].append(string)
        return anagram_dict.values()