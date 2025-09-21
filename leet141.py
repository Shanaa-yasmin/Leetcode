class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head

        while current:
            if current in visited:   # Already seen this node → cycle
                return True
            visited.add(current)     # Mark node as visited
            current = current.next   # Move forward

        return False  # Reached end → no cycle
