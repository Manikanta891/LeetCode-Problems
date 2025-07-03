class Solution:
    def permute(self, nums):
        def helper(index):
            if (index==n-1):
                res.append(nums[:])
            for j in range(index,n):
                nums[index],nums[j]=nums[j],nums[index]
                helper(index+1)
                nums[index],nums[j]=nums[j],nums[index]
        res=[]
        n=len(nums)
        helper(0)
        return res