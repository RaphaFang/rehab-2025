# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # slow and fast pointers
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        holder = None

        while fast and fast.next:
            holder = slow
            slow = slow.next
            fast = fast.next.next
        holder.next = slow.next
        
        return head
    
    # normal version 
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None  # 如果只有一個節點或空，就直接回傳 None
        
        ll = 0
        count = head
        while count:
            ll += 1
            count = count.next
        
        mid = ll//2
        cur = head
        for _ in range(mid -1):
            cur = cur.next
        cur.next = cur.next.next
        return head

# ----------------------------------------------------------------------
# 每次 cur = cur.next實際上是將cur變換成這調鏈上的下一個物件
# 這時候我修該了cur.next，理論上沒有動到head，但是會讓這調鏈的連結修改

# ----------------------------------------------------------------------
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         mark = []
#         while head:
#             mark.append(head.val)
#             head = head.next
#         mid = len(mark)//2
#         return mark[:mid] + mark[mid+1:]


        