class ListNode: 
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		node = head
		if node:
			while node.next:
				if node.val == node.next.val:
					node.next = node.next.next
				else:
					node = node.next
		return head