# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = str(self.getValue(l1) + self.getValue(l2))
        
        ll = ListNode(int(result[len(result)-1]))
        node = ll
        for i in range(len(result)-1, 0, -1):
            print result[i-1],
            node.next = ListNode(int(result[i-1]))
            node = node.next
        print 
        print self.getValue(ll)
        return result
        
    def getValue(self, link):
        if(link is None):
            return 0

        ten = 10
        node = link
        value =  node.val
        while(node.next is not None):
            value += (node.next.val * ten)
            node = node.next
            ten *= 10
        return value

solution = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)

l2 = ListNode(3)
l2.next = ListNode(4)
l2.next.next = ListNode(5)
print solution.addTwoNumbers(l1, l2)#0

l1 = ListNode(0)

l2 = ListNode(0)

print solution.addTwoNumbers(l1, l2)#0

# print solution.merge([], 0, [1], 1)#0

# print solution.merge([1,2,4,5,6], 5, [3], 1)


