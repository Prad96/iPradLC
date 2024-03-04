class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array=[]
        nums1.extend(nums2)
        merged_array=sorted(nums1)
        return statistics.median(merged_array)
        