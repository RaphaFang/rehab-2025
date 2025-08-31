# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head 

        odd = head
        even = head.next
        holder = even

        while even and even.next != None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = holder

        return head
    # 真的不太懂linklist，但似乎有一個原則，不要mass up 原先的 head
    # 也沒必要建立新的object
    # 但為什麼有時候iterate會失敗？我也不知道