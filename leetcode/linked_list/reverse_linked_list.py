from collections import deque

class Solution(object):
    def reverseList(self, head):
        backward = None
        current = head


        # 整體作法就想像，順向邊走邊拆，逆向邊走邊從新編上next
        # 拆下順向，加工成逆向
        while current:
            node_holder = current.next
            current.next = backward # 修改掉current的下一對象
            backward = current # 編寫backward
            current = node_holder

        return backward
    # --------------------------------------------------
    # 這是deque作法，但是題目要求return type ListNode
    # def reverseList(self, head):
    #     dq = deque()
    #     while head:
    #         dq.appendleft(head.val)
    #         head = head.next
    #     return dq