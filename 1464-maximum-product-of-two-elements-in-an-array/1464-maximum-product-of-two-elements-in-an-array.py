class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==2:
            return (nums[0]-1)*(nums[1]-1)
        max_product=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product=(nums[i]-1)*(nums[j]-1)
                # print(product)
                max_product=max(product,max_product)
                # print(max_product)
        return max_product
        