# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if(p is None and q is None):
            return True
        if((p is None and q is not None) or (p is not None and q is None)):
            return False
        if(p.val != q.val):
            return False
        if((p.left is None and q.left is not None) or (p.left is not None and q.left is None)):
            return False
        if((p.right is None and q.right is not None) or (p.right is not None and q.right is None)):
            return False

        if(p.left is not None and q.left is not None and not self.isSameTree(p.left, q.left)):
            return False
        if(p.right is not None and q.right is not None and not self.isSameTree(p.right, q.right)):
            return False
        return True

solution = Solution()

pp = TreeNode(2)
qq = TreeNode(2)
pp1 = TreeNode(3)
qq1 = TreeNode(3)
pp2 = TreeNode(4)
qq2 = TreeNode(4)

pp.left = pp1
pp.right = pp2

qq.left = qq1
qq.right = qq2

print solution.isSameTree(pp, qq)



pp = TreeNode(2)
qq = TreeNode(2)
pp1 = TreeNode(3)
qq1 = TreeNode(3)
pp2 = TreeNode(4)
qq2 = TreeNode(5)

pp.left = pp1
pp.right = pp2

qq.left = qq1
qq.right = qq2

print solution.isSameTree(pp, qq)


pp = TreeNode()
qq = TreeNode()
print solution.isSameTree(pp, qq)

pp = TreeNode()
qq = TreeNode(1)
print solution.isSameTree(pp, qq)