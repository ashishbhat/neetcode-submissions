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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode first = list1;
        ListNode second = list2;

        ListNode result = new ListNode();
        ListNode temp = result;

        while(first != null && second != null){
            if(first.val <= second.val){
                temp.next = first;
                first = first.next;
            }else{
                temp.next = second;
                second = second.next;
            }
            temp = temp.next;
            temp.next = null;
        }

        if(first == null){
            temp.next = second;
        }else if(second == null){
            temp.next = first;
        }
        return result.next;
    }
}