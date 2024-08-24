# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        start=head
        end=head
        
        while end and end.next:
            start=start.next
            end=end.next.next
        
        second=start
        prev=None
        while second:
            front=second.next
            second.next=prev
            prev=second
            second=front

        
        first=head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            second=second.next
            first=first.next
        return True

        