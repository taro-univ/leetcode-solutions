#Definition for singly-linked list.
from pyparsing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #slowが中間地点
        #slow以降の順序を反転する
        second = slow.next
        prev = None
        slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2