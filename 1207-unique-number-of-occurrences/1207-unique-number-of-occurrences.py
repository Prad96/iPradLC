class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        array_dict=dict()
        for element in arr:
            array_dict[element]=array_dict.get(element, 0)+1
        return len(array_dict.values())==len(set(array_dict.values()))