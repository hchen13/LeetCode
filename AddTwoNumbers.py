class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if carry:
                newNode = ListNode(1)
                return newNode
            return None
        if l1 == None:
            newNode = ListNode(l2.val)
            nl1 = None
            nl2 = l2.next
        elif l2 == None:
            newNode = ListNode(l1.val)
            nl2 = None
            nl1 = l1.next
        else:
            nl1 = l1.next
            nl2 = l2.next
            newNode = ListNode(l1.val + l2.val)
        if carry:
            newNode.val += 1
        if newNode.val >= 10:
            newNode.val %= 10
            carry = True
        else:
            carry = False
        
        newNode.next = self.add(nl1, nl2, carry)
        return newNode
    def addTwoNumbers(self, l1, l2):
        return self.add(l1, l2, False)

s = Solution()
n1 = [5]
n2 = [5]
for i in range(len(n1)-1, -1, -1):
    current = ListNode(n1[i])
    if i == len(n1) - 1:
        last = None
    current.next = last
    last = current
l1 = current
for i in range(len(n2)-1, -1, -1):
    current = ListNode(n2[i])
    if i == len(n2) - 1:
        last = None
    current.next = last
    last = current
l2 = current
l3 = s.addTwoNumbers(l1, l2)
while l3 != None:
    print l3.val,
    l3 = l3.next    

