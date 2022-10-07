class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        list=[]
        result=[0]* len(temperatures)
        for i in range(len(temperatures)):
            while list and temperatures[i]>temperatures[list[-1]]:
                index=list.pop()
                result[index]=i-index
            list.append(i)
        return result
