# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

"""
This solution uses BFS and a queue to retrieve the sum of each level in a Binary Tree
"""
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        #initialize values
        max_sum = root.val
        max_level = 1
        level = 1
        current_level = [root]
        next_level = []
        # run until it reaches an empty level
        while len(current_level) != 0:
            current_sum = 0
            # visit each node in the level
            for node in current_level:
                # add nodes value to this level's total
                current_sum += node.val
                # add notes to queue for next level
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            #copy next level's nodes by value
            current_level = next_level[:]
            next_level = []
            # compare level sums
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level
            level += 1
        return max_level

