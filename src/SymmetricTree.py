class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def isSymmetric(root):
	last = 1

def dispalyTree(root):
	if(root is None):
		return
	print root.val,
	print ' ',
	dispalyTree(root.left)
	dispalyTree(root.right)

r = TreeNode(1)
r.left=2
r.right=2

print r
print dispalyTree(r)
# print isSymmetric("{1,2,2,3,4,4,3}")
# print isSymmetric("{1,2,3,#,#,4,#,#,5}")


# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

	