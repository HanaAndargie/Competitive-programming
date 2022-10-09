class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j=0,len(people)-1
        result,temp=0,limit-people[0]
        
        while i<j:
            if people[j]>temp:
                result+=1
                j-=1
            else:
                result+=1
                i+=1
                j-=1
                remp=limit-people[i]
        if i==j:
            result+=1
        return result
