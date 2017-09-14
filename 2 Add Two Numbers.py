# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l0 = ListNode(0)
        l = l0
        carry = 0
        while l1 is not None or l2 is not None:
            add = l1.val + l2.val + carry
            l.val = add % 10
            if add >= 10:
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2 is None:
                break
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            l.next = ListNode(0)
            l = l.next
        if carry == 1:
            l.next = ListNode(carry)
        return l0

