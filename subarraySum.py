class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdic={0:1}
        sum=0
        count=0
        for i in nums:
            sum+=i
            if sum-k in sumdic:
                count+=sumdic[sum-k]
            if sum in sumdic:
                sumdic[sum]+=1
            else:
                sumdic[sum]=1
        return count
