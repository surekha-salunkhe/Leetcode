##DFS 

# 1. Preorder [print, left, right] or [root, left, right]
# 2. Inorder [left, print, right] or [left, root, right]
# 3. Postorder [left, right, print] or [left, right, root]

# Preorder 
# 1. Recursion
# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def preorder(root, res):
#     if not root:
#         return
    
#     res.append(root.val)
#     preorder(root.left, res)
#     preorder(root.right, res)

# if __name__ == '__main__':
#     # Create binary tree
#     #       1
#     #      /  \
#     #    2     3
#     #   / \     \
#     #  4   5     6
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(6)

#     res = []
#     preorder(root, res)

#     print(*res)

# #2. Iterative
# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def preOrder(root):
#     res = []

#     if not root:
#         return res
    
#     # stack = [root]
#     # while stack:
#     #     curr = stack.pop()
#     #     res.append(curr.data)

#     #     if curr.right:
#     #         stack.append(curr.right)
#     #     if curr.left:
#     #         stack.append(curr.left)
    
#     # return res

#     stack =[]
#     curr = root

#     while stack or curr:
#         while curr:
#             res.append(curr.val)
#             if curr.right:
#                 stack.append(curr.right)
#             curr = curr.left

#         if stack:
#             curr = stack.pop()
        
#     return res

# if __name__ == '__main__':
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     res = preOrder(root)
#     print(' '.join(map(str, res)))


#Inorder
##1. Recursion
# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def inOrder(node, res):
#     if node is None:
#         return

#     # Traverse the left subtree first
#     inOrder(node.left, res)

#     # Visit the current node
#     res.append(node.data)

#     # Traverse the right subtree last
#     inOrder(node.right, res)

# if __name__ == "__main__":
#     # Create binary tree
#     #       1
#     #      /  \
#     #    2     3
#     #   / \     \
#     #  4   5     6
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.right = Node(6)

#     res = []
#     inOrder(root, res)

#     for node in res:
#         print(node, end=" ")


# #2. Iterative
# # [Naive Approach] Using Stack - O(n) Time and O(h) Space
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def inorder(root):
#     res = []
#     stack = []
#     curr = root

#     while stack or curr:
#         # go to the leftmost node
#         while curr:
#             stack.append(curr)
#             curr = curr.left

#         # backtrack
#         curr = stack.pop()
#         res.append(curr.val)
#         curr = curr.right

#     return res

# if __name__ == '__main__':
#     # Binary tree
#     #       1
#     #      / \
#     #     2   3
#     #    / \
#     #   4   5
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)

#     res = inorder(root)
#     print(' '.join(map(str, res)))  # Output: 4 2 5 1 3

## Morris Traversal Algorithm (O(n) time and O(1) space)
#No stack no recursion
#Idea based on "Threaded Binary Tree"
#1. Create links to inorder successor
#2. Print data using these links
#3. Revert the changes to restore original tree
