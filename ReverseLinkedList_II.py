class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        head = dummy
        
        for i in range(1,m):
            if not head:
                return head
            head = head.next
        
        pre_m_node = head
        m_node = head.next
        n_node = m_node
        post_n_node = n_node.next
        
        for i in range(m,n):
            temp = post_n_node.next
            post_n_node.next = n_node
            n_node = post_n_node
            post_n_node = temp
        
        m_node.next = post_n_node
        pre_m_node.next = n_node
        
        return dummy.next