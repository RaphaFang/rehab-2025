
import java.lang.classfile.components.ClassPrinter;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head;
        ListNode fast = head;
        ListNode holder = null;

        while (fast != null && fast.next != null) {
            holder = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        holder.next = slow.next;
        return head;
    }
}
// class Solution:
// # slow and fast pointers
// def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
// if not head or not head.next:
// return None

// slow, fast = head, head
// holder = None

// while fast and fast.next:
// holder = slow
// slow = slow.next
// fast = fast.next.next
// holder.next = slow.next

// return head