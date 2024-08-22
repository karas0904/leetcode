# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        temp=head
        dic={}

        while temp is not None:

            if temp in dic:
                return True
            else:
                dic[temp]=1
            
            temp=temp.next
        return False
        