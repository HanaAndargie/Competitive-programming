class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        popped.reverse()
        for i in pushed:
            stack.append(i)
            while len(stack)!=0 and len(popped)!=0 and stack[-1]==popped[-1]:
                stack.pop()
                popped.pop()
        return len(stack)==0
