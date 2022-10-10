class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prevSum=0
        total=sum(nums)
        for i in range(len(nums)):
            rightSum=total-nums[i]-prevSum
            if prevSum==rightSum:
                return i
            prevSum+=nums[i]
        return -1
