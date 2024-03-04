class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merged_array=[]
        # merged_array.extend()
        return statistics.median(nums1+nums2)
        