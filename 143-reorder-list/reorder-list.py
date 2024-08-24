# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow=head
        fast=slow.next


        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is None or fast.next is None:
                break
        first=head
        second=slow.next
        slow.next=None

        prev=None
        while(second is not None):
            front=second.next
            second.next=prev
            prev=second
            second=front

        first = head
        second = prev
        while (second):
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
