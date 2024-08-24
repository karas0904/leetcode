# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1=headA
        temp2=headB

        dic={}

        while temp1 or temp2:
            if temp1: 
                if temp1 not in dic:
                    dic[temp1] = 1  
                else:
                    return temp1  
                temp1 = temp1.next  

            if temp2:  
                if temp2 not in dic:
                    dic[temp2] = 1  
                else:
                    return temp2  
                temp2 = temp2.next 

        return None 


        