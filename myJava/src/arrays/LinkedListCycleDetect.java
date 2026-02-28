package arrays;

public class LinkedListCycleDetect {
    /*
     * Given the beginning of a linked list head, return true if there is a cycle in
     * the linked list. Otherwise, return false.
     * 
     * There is a cycle in a linked list if at least one node in the list can be
     * visited again by following the next pointer.
     * 
     * Internally, index determines the index of the beginning of the cycle, if it
     * exists. The tail node of the list will set it's next pointer to the index-th
     * node. If index = -1, then the tail node points to null and no cycle exists.
     * 
     * Note: index is not given to you as a parameter.
     * 
     * Example 1:
     * Input: head = [1,2,3,4], index = 1
     * Output: true
     * Explanation: There is a cycle in the linked list, where the tail connects to
     * the 1st node (0-indexed).
     * 
     * Example 2:
     * Input: head = [1,2], index = -1
     * Output: false
     * 
     * Constraints:
     * 0 <= Length of the list <= 1000.
     * -1000 <= Node.val <= 1000
     * index is -1 or a valid index in the linked list.
     * 
     */

    // Fast and slow pointer
    // slow = slow.next
    // fast = fast.next.next

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

    // =========================
    // Create cycle based on index
    // index = position where tail connects
    // index = -1 → no cycle
    // =========================
    public static void createCycle(ListNode<Integer> head, int index) {
        if (head == null || index == -1)
            return;

        ListNode<Integer> curr = head;
        ListNode<Integer> cycleNode = null;
        int i = 0;

        while (curr.next != null) {
            if (i == index) {
                cycleNode = curr;
            }
            curr = curr.next;
            i++;
        }

        // curr is now tail
        if (i == index) {
            cycleNode = curr;
        }

        // Connect tail to index node
        curr.next = cycleNode;
    }

    // =========================
    // Safe print (limit to avoid infinite loop)
    // =========================
    public static <T> void printList(ListNode<Integer> head, int limit) {
        ListNode<Integer> curr = head;
        int count = 0;

        while (curr != null && count < limit) {
            System.out.print(curr.val + " -> ");
            curr = curr.next;
            count++;
        }

        System.out.println(count == limit ? "..." : "null");
    }

    public static boolean detectCycle(ListNode<Integer> head) {
        ListNode<Integer> slow = head;
        ListNode<Integer> fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4 };
        int index = 1;

        ListNode<Integer> head = createList(arr);

        createCycle(head, index);

        System.out.println("Original list: ");
        printList(head, 10);

        boolean res = detectCycle(head);
        System.out.println("Cycle exists: " + res);

    }

}
