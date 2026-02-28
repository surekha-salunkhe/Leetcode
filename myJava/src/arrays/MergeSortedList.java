package arrays;

public class MergeSortedList {

    /*
     * You are given the heads of two sorted linked lists list1 and list2.
     * Merge the two lists into one sorted linked list and return the head of the
     * new sorted linked list.
     * The new list should be made up of nodes from list1 and list2.
     * 
     * Example 1:
     * Input: list1 = [1,2,4], list2 = [1,3,5]
     * Output: [1,1,2,3,4,5]
     * 
     * Example 2:
     * Input: list1 = [], list2 = [1,2]
     * Output: [1,2]
     * 
     * Example 3:
     * Input: list1 = [], list2 = []
     * Output: []
     * 
     * Constraints:
     * 0 <= The length of the each list <= 100.
     * -100 <= Node.val <= 100
     * 
     */

    static class ListNode<T> {
        T val;
        ListNode<T> next;

        ListNode(T val) {
            this.val = val;
            this.next = null;
        }
    }

    public static ListNode<Integer> createList(int[] arr) {
        if (arr == null || arr.length == 0) {
            return null;
        }

        ListNode<Integer> head = new ListNode<>(arr[0]);
        ListNode<Integer> curr = head;

        for (int i = 1; i < arr.length; i++) {
            curr.next = new ListNode<>(arr[i]);
            curr = curr.next;
        }
        return head;

    }

    public static <T> void printList(ListNode<T> head) {
        ListNode<T> curr = head;
        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println("null");
    }

    public static ListNode<Integer> mergeSortedLists(ListNode<Integer> head1, ListNode<Integer> head2) {
        ListNode<Integer> dummy = new ListNode<>(0);
        ListNode<Integer> node = dummy;

        while (head1 != null && head2 != null) {
            if (head1.val < head2.val) {
                node.next = head1;
                head1 = head1.next;
            } else {
                node.next = head2;
                head2 = head2.next;
            }
            node = node.next;
        }
        // if anything left after reaching null from any list
        if (head1 != null) {
            node.next = head1;
        } else {
            node.next = head2;
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        int[] arr1 = { 0, 1, 4, 6 };
        int[] arr2 = { 2, 3, 5, 7 };

        // create List
        ListNode<Integer> head1 = createList(arr1);
        ListNode<Integer> head2 = createList(arr2);

        System.out.println("1st sorted list: ");
        printList(head1);

        System.out.println("2nd sorted list: ");
        printList(head2);

        System.out.println("Merged sorted list: ");
        ListNode<Integer> head = mergeSortedLists(head1, head2);
        printList(head);

    }

}
