# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return self.depth(root, 0)

    def depth(self, root, lens):
        if(root is None):
            return lens
        left,right = lens,lens
        if(root.left is not None):
            left = self.depth(root.left, lens +1)
        if(root.right is not None):
            right = self.depth(root.right, lens +1)
        if(root.left is None and root.right is None):
            return lens+1
        return max(left, right)

solution = Solution()

pp = TreeNode(2)
pp1 = TreeNode(3)
pp2 = TreeNode(4)
pp3 = TreeNode(4)
pp4 = TreeNode(4)
pp5 = TreeNode(4)
pp6 = TreeNode(4)

pp.left = pp1
pp.right = pp2

pp1.left = pp3
pp1.right = pp4

pp3.left = pp5
pp5.right=pp6

print solution.maxDepth(pp)

pp = TreeNode(2)
pp1 = TreeNode(3)
pp2 = TreeNode(4)
pp3 = TreeNode(4)
pp4 = TreeNode(4)
pp5 = TreeNode(4)
pp6 = TreeNode(4)

pp.left = pp1
pp.right = pp2

pp2.left = pp3

print solution.maxDepth(pp)

pp = TreeNode(2)

print solution.maxDepth(pp)
