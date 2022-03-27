from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start, end = 1, 1
        current_node = head

        # 링크드 리스트의 전체길이 확인
        while current_node is not None:
            current_node = current_node.next
            end += 1

        current_node = head
        while start < end-n-1 and start != end-n-1:
            # 삭제할 노드의 위치가 중간에 있는 경우
            current_node = current_node.next
            start += 1
        
        if end-n-1 == 0:
            # 삭제할 노드가 맨 앞에 있는 경우
            current_node = current_node.next
            return current_node
        else:
            new_node = current_node.next.next
            current_node.next = new_node
            return head