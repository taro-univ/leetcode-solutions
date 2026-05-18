# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #ポインタの概念が登場
        #メモリ上に連続して配置するのではなく、次のデータへの行き先を各データが持つ
        #headが手掛かり、見失うとリストにアクセスできなくなる
        #アクセスにはO(n)だが、挿入、削除が非常に楽という特徴がある

        prev = None
        curr = head

        while curr:
            nxt = curr.next

            curr.next = prev

            prev = curr

            curr = nxt

        return prev