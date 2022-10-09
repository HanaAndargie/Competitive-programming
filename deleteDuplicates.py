# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        prev=result=None
        curr=head
        while curr:
            is_dup=False
            while curr.next and curr.val==curr.next.val:
                curr=curr.next
                is_dup=True
            if is_dup:
                curr=curr.next
                continue
            if not prev:
                prev=result=curr
            else:
                prev.next=curr
                prev=curr
            curr=curr.next
        return result
        
