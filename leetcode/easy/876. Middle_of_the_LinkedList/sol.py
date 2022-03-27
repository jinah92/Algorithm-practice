# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        search_nodes = head
        while search_nodes is not None:
            search_nodes = search_nodes.next
            idx += 1
        start_idx = int(idx / 2)  # middle_node 헤더 위치
        
        idx = 0
        while idx != start_idx:
            head = head.next
            idx += 1
        
        return head