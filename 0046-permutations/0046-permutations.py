class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        permutation=itertools.permutations(nums)
        for perm in permutation:
            permutations.append(perm)
        return permutations