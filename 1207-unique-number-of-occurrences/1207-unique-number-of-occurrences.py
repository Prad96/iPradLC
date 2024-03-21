class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        array_dict=dict()
        for element in arr:
            array_dict[element]=array_dict.get(element, 0)+1
        values=list(array_dict.values())
        return len(values)==len(set(values))