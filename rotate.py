class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        temp=[0]*len(nums)
        
        for i in range(len(nums)):
            j=nums[i]
            new_index=(i+k)%len(nums)
            
            temp[new_index]=j
        nums[:]=temp
        
