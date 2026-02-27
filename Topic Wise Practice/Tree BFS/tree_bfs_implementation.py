#BFS Level order traversal - Binary Tree

## 1. Recursion
# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def level_order_rec(root, level, res):
#     if not root:
#         return
    
#     #add a new level to result if needed
#     if len(res) <= level:
#         res.append([])

#     res[level].append(root.val)

#     level_order_rec(root.left, level + 1, res)
#     level_order_rec(root.right, level + 1, res)

# def level_order(root):
#     res = []
#     level_order_rec(root, 0, res)
#     return res


# if __name__ == '__main__':
#     #       5
#     #    /    \
#     #   12     13 
#     #  /   \    \
#     #  7    14   2
#     #/  \  /  \ /  \
#     #17 23 27 3 8  11

#     root = Node(5)
#     root.left = Node(12)
#     root.right = Node(13)

#     root.left.left = Node(7)
#     root.left.right = Node(14)

#     root.right.right = Node(2)

#     root.left.left.left = Node(17)
#     root.left.left.right = Node(23)

#     root.left.right.left = Node(27)
#     root.left.right.right = Node(3)

#     root.right.right.left = Node(8)
#     root.right.right.right = Node(11)

#     res = level_order(root)

#     for level in res:
#         print(' '.join(map(str, level)))


# ## 2. Queue Iterative
# from collections import deque

# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.left = None
#         self.right = None

# def level_order(root):

#     if not root:
#         return []

#     queue = deque([root])
#     curr_level = 0
#     res = []

#     while queue:
#         n = len(queue)
#         res.append([])

#         for _ in range(n):
#             curr = queue.popleft()
#             res[curr_level].append(curr.val)

#             if curr and curr.left:
#                 queue.append(curr.left)

#             if curr and curr.right:
#                 queue.append(curr.right)
#         curr_level += 1
#     return res

# if __name__ == '__main__':
#     #       5
#     #    /    \
#     #   12     13 
#     #  /   \    \
#     #  7    14   2
#     #/  \  /  \ /  \
#     #17 23 27 3 8  11

#     root = Node(5)
#     root.left = Node(12)
#     root.right = Node(13)

#     root.left.left = Node(7)
#     root.left.right = Node(14)

#     root.right.right = Node(2)

#     root.left.left.left = Node(17)
#     root.left.left.right = Node(23)

#     root.left.right.left = Node(27)
#     root.left.right.right = Node(3)

#     root.right.right.left = Node(8)
#     root.right.right.right = Node(11)

#     res = level_order(root)

#     for level in res:
#         print(' '.join(map(str, level)))
