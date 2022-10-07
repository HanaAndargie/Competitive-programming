class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed=sorted(list(zip(position,speed)),reverse=True)
        prev_time=0
        count=0
       
        for p,s in  posSpeed:
            t=(target - p ) /s
            if t > prev_time:
                count+=1
                prev_time=t
        return count
        
