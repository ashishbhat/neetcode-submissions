/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        if(head == null){
            return false;
        }

        while(fast != null && fast.next != null){

            System.out.println("Hello");
            fast = fast.next.next;
            slow = slow.next;
            if(fast == slow){
                return true;
            }
            System.out.println(fast);

        }
        return false;
    }
}
