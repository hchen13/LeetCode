class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __str__(self):
		return str(self.val)


class Solution:
	def reverseBetween(self, head, m, n):
		front = ListNode(0)
		front.next = head
		next_node = head
		before = front
		last = front
		order = 1
		while next_node:
			current = next_node
			if order == m:
				before = last
				m_node = current
			next_node = current.next
			if order in range(m+1, n+1):
				if order == n:
					m_node.next = current.next

				current_next = before.next
				before.next = current
				current.next = current_next

			last = current
			order += 1
		return front.next


def print_list(head):
	ptr = head
	while ptr:
		print ptr.val
		ptr = ptr.next


head = ListNode(1)
current = head
for i in range(2, 10):
	node = ListNode(i)
	current.next = node
	current = node



s = Solution()
new = s.reverseBetween(head, 1, 7)
print_list(new)