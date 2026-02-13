# Build a linkedList, traverse, add, delete
# Part 1: Traverse and modify [1-10] - Done
# Part 2: Insertion and Deletion [11-15]
# Part 3: Reversal Variations [16-20]
# Part 4: Reordering [21-]25]
# Part 5: Merging [26-30]
# Part 6: Special structures [31-35]


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def create_Node(data):
#     node = Node(data)
#     # print(node.data)
#     return node

# def traverse(head):
#     if head:
#         curr = head
#         while curr:
#             print(curr.data, end= ' -> ')
#             curr = curr.next
#         print('None')

# def add_node_at_start(head, newnode):
#     # if head is None: # This is incorrect as we should be able to add to empty list
#     #     return None
    
#     if newnode is None:
#         return head
    
#     newnode.next = head
#     # head = newnode # newnode is the new head
#     return newnode

# def add_node_after(node, newnode):
#     if node:
#         newnode.next = node.next
#         node.next = newnode 

# def del_after_node(node):
#     if node and node.next:
#         temp = node.next
#         node.next = temp.next
#         temp.next = None

# def del_node_by_value(head, value):
#     if head is None:
#         return None

#     # if node is head, we want to remove head
#     if value == head.data:
#         temp = head.next
#         head.next = None
#         return temp
    
#     # node is not head, other than head, 
#     curr = head
#     while curr.next and curr.next.data != value: #curr.next exists and is not equal to del node we traverse
#         curr = curr.next

#     if curr.next:
#         del_after_node(curr)
    
#     return head


# def main():
#     head = create_Node(1)
#     head.next = create_Node(2)
#     head.next.next = create_Node(3)
#     head.next.next.next = create_Node(4)
#     traverse(head)
#     head = add_node_at_start(head, Node(0))
#     traverse(head)
#     add_node_after(head.next.next, Node(2.5))
#     traverse(head)
#     # del_after_node(head.next.next)
#     # traverse(head)
#     del_node_by_value(head, 2.5)
#     traverse(head)


# if __name__ == "__main__":
#     main()


############################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    curr = head
    out = []
    while curr:
        out.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(out) + " -> NULL")

## Part 1: Basic Traversal and Modification

### Problem 1: Reverse Linked List
# Reverse a singly linked list.

# ```
# Input:  1 → 2 → 3 → 4 → 5 → NULL
# Output: 5 → 4 → 3 → 2 → 1 → NULL
# ```

# **Pattern:** Track three pointers: `prev`, `curr`, `next`. At each step, reverse the link.


# def reverse_ll(head):
#     curr = head
#     prev = None

#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev

# def main():
#     arr = [1,2,3,4,5]
#     head = build_linked_list(arr)
#     ans = reverse_ll(head)
#     print_list(ans)


# if __name__ == "__main__":
#     main()

############################################################################
# ### Problem 2: Delete Node in a Linked List

# Delete a node (not the tail) given only access to that node.

# ```
# Input:  4 → 5 → 1 → 9, node = 5
# Output: 4 → 1 → 9
# ```

# **Trick:** Copy the next node's value into current node, then skip the next node.

# def my_func(node):

#     node.val = node.next.val
#     node.next = node.next.next

# def find_node(head, target):
#     curr = head
#     while curr:
#         if curr.val == target:
#             return curr
#         curr = curr.next
#     return None

# def main():
#     arr = [4,5,1,9]
#     head = build_linked_list(arr)
#     node = find_node(head, 5)
#     my_func(node)
#     print_list(head)


# if __name__ == "__main__":
#     main()

#####################################################################################
# ### Problem 3: Remove Linked List Elements

# # Remove all nodes with a given value.

# # ```
# # Input:  1 → 2 → 6 → 3 → 4 → 5 → 6, val = 6
# # Output: 1 → 2 → 3 → 4 → 5
# # ```

# # **Hint:** Use a dummy head to handle the case where head itself needs removal.

# def my_func(head, target):
#     dummy = ListNode(0)
#     dummy.next = head
#     prev, curr = dummy, head

#     while curr:
#         if curr.val == target:
#             prev.next = curr.next
#         else:
#             prev = curr
#         curr = curr.next

#     return dummy.next

# def main():
#     arr = [1,2,6,3,4,5,6]
#     val = 6
#     head = build_linked_list(arr)
#     ans = my_func(head, val)
#     print_list(ans)


# if __name__ == "__main__":
#     main()

#####################################################################################
# # ### Problem 4: Remove Duplicates from Sorted List

# # Delete all duplicates in a sorted list (keep one of each).

# # ```
# # Input:  1 → 1 → 2 → 3 → 3
# # Output: 1 → 2 → 3

# def my_func(head):
#     curr = head
#     while curr and curr.next:
#         if curr.val == curr.next.val:
#             curr.next = curr.next.next
#         else: #if we dont keep it in else then 1, 1, 1 fails
#             curr = curr.next
#     return head

# def main():
#     arr = [1,1,1,2,3,4]
#     head = build_linked_list(arr)
#     ans = my_func(head)
#     print_list(ans)


# if __name__ == "__main__":
#     main()
#####################################################################################
### Problem 5: Remove Duplicates from Sorted List II

# Delete all nodes that have duplicates (keep none of them).

# ```
# Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
# Output: 1 → 2 → 5

# Input:  1 → 1 → 1 → 2 → 3
# Output: 2 → 3

# def my_func(head):
#     dummy = ListNode(0)
#     dummy.next = head
#     prev, curr = dummy, head
#     while curr:
#         while curr.next and curr.val == curr.next.val:
#             curr = curr.next
        
#         if prev.next == curr:
#             prev = prev.next
#         else:
#             prev.next = curr.next
        
#         curr = curr.next
#     return dummy.next


# def main():
#     arr = [1,1,1,2,3]
#     head = build_linked_list(arr)
#     ans = my_func(head)
#     print_list(ans)


# if __name__ == "__main__":
#     main()
#####################################################################################

# ### Problem 6: Middle of the Linked List
# # Return the middle node. If two middle nodes, return the second.

# # ```
# # Input:  1 → 2 → 3 → 4 → 5
# # Output: Node 3

# # Input:  1 → 2 → 3 → 4 → 5 → 6
# # Output: Node 4
# # ```

# # **Pattern:** Slow pointer moves 1 step, fast pointer moves 2 steps. When fast reaches end, slow is at middle.

# def my_func(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow  = slow.next
#         fast = fast.next.next

#     return slow

# def main():
#     arr = [1,2,3,4,5]
#     head = build_linked_list(arr)
#     ans = my_func(head)
#     print_list(ans)


# if __name__ == "__main__":
#     main()

#####################################################################################
# ### Problem 7: Linked List Cycle

# # Determine if a linked list has a cycle.

# # ```
# # Input:  3 → 2 → 0 → -4 → (back to 2)
# # Output: True
# # ```

# # **Pattern:** Fast/slow pointers. If they meet, there's a cycle.

# def my_func(head):
#     slow = fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True
#     return False


# def main():
#     arr = [3,2,0,-4]

#     head = build_linked_list(arr)

#     pos = 1  # tail connects to index 1 (value 2)

#     # create the cycle
#     tail = head
#     join = None
#     idx = 0

#     while tail.next:
#         if idx == pos:
#             join = tail
#         tail = tail.next
#         idx += 1

#     # check last node index
#     if idx == pos:
#         join = tail

#     tail.next = join

#     ans = my_func(head)
#     print(ans)


# if __name__ == "__main__":
#     main()


#####################################################################################
# ### Problem 8: Linked List Cycle II

# # Return the node where the cycle begins, or null if no cycle.

# # ```
# # Input:  3 → 2 → 0 → -4 → (back to 2)
# # Output: Node 2
# # ```

# # **Pattern:** After fast and slow meet, reset one to head. Move both at same speed — they meet at cycle start.

# def my_func(head):
#     slow = fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             slow = head
#             break

#     while True:
#         slow = slow.next
#         fast = fast.next

#         if slow == fast:
#             return slow
        

# def main():
#     arr = [3, 2, 0, -4]

#     head = build_linked_list(arr)

#     pos = 1  # tail connects to index 1 (value 2)

#     # create the cycle
#     tail = head
#     join = None
#     idx = 0

#     while tail.next:
#         if idx == pos:
#             join = tail
#         tail = tail.next
#         idx += 1

#     # check last node index
#     if idx == pos:
#         join = tail

#     tail.next = join  # create the cycle

#     ans = my_func(head)  # will return the node where cycle begins
#     print(ans.val)  # optionally print ans.val if you want the value


# if __name__ == "__main__":
#     main()

#####################################################################################
# ### Problem 9: Intersection of Two Linked Lists

# # Find the node where two lists intersect, or null if they don't.

# # ```
# # List A:      4 → 1 ↘
# #                     8 → 4 → 5
# # List B: 5 → 6 → 1 ↗
# # Output: Node 8

# # **Hint:** After reaching the end of one list, continue from the head of the other. 
# # They'll meet at intersection or both reach null.

# def my_func(headA, headB):
#     pA = headA
#     pB = headB

#     while pA != pB:
#         pA = pA.next if pA else headB
#         pB = pB.next if pB else headA

#     return pA


# def main():
#     # List A values before intersection
#     listA_vals = [4, 1]
#     # List B values before intersection
#     listB_vals = [5, 6, 1]
#     # Shared intersection values
#     intersection_vals = [8,4,5]

#     # Build intersection part
#     intersection_head = build_linked_list(intersection_vals)

#     # Build list A and attach intersection
#     headA = build_linked_list(listA_vals)
#     if headA:
#         tail = headA
#         while tail.next:
#             tail = tail.next
#         tail.next = intersection_head
#     else:
#         headA = intersection_head

#     # Build list B and attach intersection
#     headB = build_linked_list(listB_vals)
#     if headB:
#         tail = headB
#         while tail.next:
#             tail = tail.next
#         tail.next = intersection_head
#     else:
#         headB = intersection_head

#     # Call your function
#     ans = my_func(headA, headB)

#     # Print result
#     if ans:
#         print(ans.val)
#     else:
#         print(None)


# if __name__ == "__main__":
#     main()

# #####################################################################################
# # ### Problem 10: Palindrome Linked List

# # Check if a linked list is a palindrome.

# # ```
# # Input:  1 → 2 → 2 → 1
# # Output: True

# # Input:  1 → 2
# # Output: False
# # ```

# # **Approach:** Find middle, reverse second half, compare both halves.
# def my_func(head):

#     slow = fast = head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     prev = None
#     curr = slow

#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt

#     first = head      # 1 → 2
#     second = prev     # 1 → 2
#     while second:
#         if first.val != second.val:
#             return False
#         first = first.next
#         second = second.next
    
#     return True

# def main():
#     arr = [1,2,2,1]
#     head = build_linked_list(arr)
#     print(my_func(head))
#     # print_list(ans)


# if __name__ == "__main__":
#     main()
# #####################################################################################


