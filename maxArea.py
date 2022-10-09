class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        temp_area=0
        head=0
        tail=len(height)-1
        for i in range(len(height)):
            width=tail-head
            if height[head]<height[tail]:
                temp_area=width*height[head]
                head=head+1
            else:
                temp_area=width*height[tail]
                tail=tail-1
            max_area=max(max_area,temp_area)
        return max_area
