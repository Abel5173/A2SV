class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dN = ListNode()
        head = dN
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                head.next = p1
                p1 = p1.next
            else:
                head.next = p2.next
                p2 = p2.next
            head = head.next
        if p1:
            head.next = p1
        if p2:
            head.next = p2
        
        return dN.next