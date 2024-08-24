# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        currentnode=head
        prev=None

        count=0


        temp = head
        for _ in range(k):
            if temp is None:
                return head
            temp = temp.next

            
        while(count<k and currentnode is not None):
            frontnode=currentnode.next
            currentnode.next=prev
            prev=currentnode
            currentnode=frontnode
            count+=1
        
        if frontnode is not None:
            head.next = self.reverseKGroup(frontnode, k)
        return prev

        