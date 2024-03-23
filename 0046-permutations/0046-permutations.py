class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        for permutation in itertools.permutations(nums):
            permutations.append(permutation)
        return permutations