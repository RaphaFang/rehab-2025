class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_1 = []
        status = True
        while status:
            list_1.append(head.val)
            head = head.next
            if not head:
                status = False

        ll = len(list_1)
        mm = 0
        for i in range(int(ll/2)):
            mm = max(mm, list_1[i] + list_1[ll -1 -i])
        return (mm)