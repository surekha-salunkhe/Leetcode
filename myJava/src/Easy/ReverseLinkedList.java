package Easy;

public class ReverseLinkedList {

    /*
     * Given the beginning of a singly linked list head, reverse the list, and
     * return the new beginning of the list.
     * 
     * Example 1:
     * Input: head = [0,1,2,3]
     * Output: [3,2,1,0]
     * 
     * Example 2:
     * Input: head = []
     * Output: []
     * 
     * Constraints:
     * 0 <= The length of the list <= 1000.
     * -1000 <= Node.val <= 1000
     */

    // T = generic data type, type decided when object is created, Reusable design,
    // type safety, no casting, clean architecture

    // ==============================
    // 1.Generic Node Definition
    // ==============================
    static class ListNode<T> {
        T val;
        ListNode<T> next;

        ListNode(T val) {
            this.val = val;
            this.next = null;
        }
    }
    // In interviews:
    // class ListNode {
    // int val;
    // ListNode next;
    // }

    // ==============================
    // 2. Create LinkedList from array
    // ==============================
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

    // ==============================
    // 3. Print LinkedList
    // ==============================
    public static <T> void printList(ListNode<T> head) {
        ListNode<T> curr = head;
        while (curr != null) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
        }
        System.out.println("null");
    }

    // 4. Reverse LinkedList
    public static <T> ListNode<T> reverseList(ListNode<T> head) {
        ListNode<T> prev = null;
        ListNode<T> curr = head;

        while (curr != null) {
            ListNode<T> temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }

        return prev;
    }

    // ==============================
    // 5. Main Method (Test Harness)
    // ==============================
    public static void main(String[] args) {
        int[] arr = {};
        // Create list
        ListNode<Integer> head = createList(arr);

        System.out.println("Original List: ");
        printList(head);

        // call method
        head = reverseList(head);
        System.out.println("Reversed List: ");
        printList(head);

    }

}
