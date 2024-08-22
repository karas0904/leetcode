# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        
        current=head
        len=1
        while current.next:
            current=current.next
            len+=1
        
        l_node=current

        k=k%len
        if k==0:
            return head
        
        new_tail_pos = len - k
        current = head
        for i in range(new_tail_pos - 1):
            current = current.next

        new_head=current.next
        current.next=None
        l_node.next=head

        return new_head
            