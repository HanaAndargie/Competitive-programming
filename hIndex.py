class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() # [0,1,3,5,6]
        result=0
        if max(citations)>=1:
            #result=1
            for i in range(len(citations)):
                i=len(citations)-i-1
                if result < citations[i]:
                    result=result+1
        return result
