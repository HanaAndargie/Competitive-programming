class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        if nums.count(0)>1:
            return[0]*len(nums)
        prod=1
        for i in nums:
            if i!=0:
                prod=prod*i
        if nums.count(0)==1:
            ans=[0]*len(nums)
            ind=nums.index(0)
            ans[ind]=prod
            return ans
        for j in range(len(nums)):
            nums[j]=prod//nums[j]
        return nums
