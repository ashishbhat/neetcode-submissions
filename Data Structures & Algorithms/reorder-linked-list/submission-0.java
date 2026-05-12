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
    public void reorderList(ListNode head) {
        ListNode first = head;
        ListNode second = head.next;
        Deque<ListNode> stack = new ArrayDeque<>();

        ListNode temp = head;
        while(temp != null){
            stack.offerLast(temp);
            temp = temp.next;
        }

        while(true){
            ListNode tos = stack.pollLast();
            tos.next = null;
            if(tos == second || tos == first){
                break;
            }
            System.out.println(tos.val);
            first.next = tos;
            tos.next = second;
            first = second;
            second = second.next;

        }        
    }
}