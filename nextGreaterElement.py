class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list,dec=[],{}
        for i in nums2:
            while list and list[-1]<i: dec[list.pop()]=i
            list.append(i)
        return [dec.get(i,-1)for i in nums1]
