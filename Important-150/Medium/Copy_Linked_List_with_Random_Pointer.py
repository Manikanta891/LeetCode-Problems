class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # First pass: Copy all nodes and build a map from original -> copy
        old_to_new = {}

        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Second pass: Set next and random pointers
        current = head
        while current:
            copy_node = old_to_new[current]
            copy_node.next = old_to_new.get(current.next)
            copy_node.random = old_to_new.get(current.random)
            current = current.next

        # Return the copied head
        return old_to_new[head]


# 🚀 Problem Summary:
# Given: A linked list where each node has a `.next` and `.random` pointer
# Goal: Deep-copy the list so that both `next` and `random` pointers are preserved correctly

# 🧩 Brute Force Idea:
# - For each node, create a new node and find the mapping manually using two passes
# - But tracking `random` without mapping is tough and inefficient

# ⚡ Optimization / Pattern Used:
# Pattern: Hash Map (Original Node → Copied Node)
# Pass 1: Create clone nodes and store mapping
# Pass 2: Connect `.next` and `.random` using this mapping

# 🔑 Key Insight:
# We can’t connect `.random` immediately unless we store the mapping
# So we do two passes: build copies first, connect pointers later using the map

# 🧠 Why it works:
# All original nodes are uniquely hashable — so we can store their corresponding clone nodes
# Once all nodes are copied, we can assign `.next` and `.random` based on the original’s mapping

# 📈 Time & Space Complexity:
# Time: O(n) — Two passes over the list
# Space: O(n) — Extra space for mapping (hash map)

# 📝 My Takeaway:
# ✅ When dealing with complex pointer structures, **building a mapping is key**
# ✅ This problem teaches how to separate node creation and pointer connection phases
# ✅ There’s an advanced O(1) space version too (interleaving copy nodes), but this is cleaner and safer for interviews
