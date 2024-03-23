class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        narray,combinations=[],[]
        for i in range(1, n+1):
            narray.append(i)
        for combination in itertools.combinations(narray,k):
            combinations.append(combination)
        return combinations