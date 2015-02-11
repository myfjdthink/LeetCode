# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if(head is None):
            return None
        if(head.next is None):
            self.showLink(head)
            return head
        pre = head
        present = head.next
        
        node = head
        while(node.next is not None):
            pre = node
            present = node.next
            if(pre.val == present.val):
                print 'eeeee'
                if(present.next is not None):
                    print 'HH',pre.next.val, present.next.val
                    pre.next = present.next
                else:
                    pre.next = None
            else:
                node = node.next

        self.showLink(head)
        return head
        
    def showLink(self, head):
        node = head
        while(node.next):
            print node.val
            node = node.next
        print node.val

solution = Solution()

pp = ListNode(2)
pp1 = ListNode(3)
pp2 = ListNode(4)
pp3 = ListNode(4)
pp4 = ListNode(4)
pp5 = ListNode(6)
pp6 = ListNode(7)

pp.next = pp1
pp1.next = pp2
pp2.next = pp3
pp3.next = pp4
pp4.next = pp5
pp5.next=pp6

# solution.deleteDuplicates(pp)

pp = ListNode(2)
pp1 = ListNode(2)
pp.next = pp1
print solution.deleteDuplicates(pp)

solution.deleteDuplicates(None)
