import org.w3c.dom.NodeList;

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode backward = null;
        ListNode current = head;

        while (current != null) {
            ListNode nodeHolder = current.next;
            current.next = backward;
            backward = current;
            current = nodeHolder;
        }
        return backward;
    }
}