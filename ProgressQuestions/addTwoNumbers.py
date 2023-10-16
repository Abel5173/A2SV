# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1.next
        s1 = ''
        while c1:
           s1 += str(c1.val)
           c1 = c1.next
print(Solution().addTwoNumbers([2,4,3],[5,6,4]))