class TimeMap:
    def __init__(self):
        self.store = {}  # key -> [timestamps], [values]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[], []]  # [timestamps], [values]
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        times, values = self.store[key]
        left, right = 0, len(times) - 1
        best_index = -1

        # Binary Search: Find the largest time <= timestamp
        while left <= right:
            mid = (left + right) // 2
            if times[mid] <= timestamp:
                best_index = mid
                left = mid + 1  # move right to find later value
            else:
                right = mid - 1  # move left

        if best_index == -1:
            return ""
        return values[best_index]



# 🚀 Problem Summary:
# Design a class `TimeMap` that supports:
# - set(key, value, timestamp): Store the key with value and timestamp
# - get(key, timestamp): Return the value with the **highest timestamp ≤ given timestamp**

# 🧩 Brute Force Idea:
# Store all (key, value, timestamp) tuples
# On `get`, linearly search all timestamps ≤ given timestamp
# Time: O(n) for each get (slow if many entries)
# Space: O(n)

# ⚡ Optimization / Pattern Used:
# Pattern: Hash Map + Binary Search
# Store in `self.store` → key → [timestamps], [values]
# - Use `bisect_right` logic (or manual binary search) to find latest timestamp ≤ input
# - On `get`, use binary search to get result in O(log n)

# 🔑 Key Insight:
# Each key maps to **sorted timestamps**, so binary search is valid
# We store timestamps and corresponding values separately for easy indexing

# 🧠 Why it works:
# Since timestamps are inserted in increasing order,
# you can use binary search to efficiently fetch the right value (≤ timestamp)

# 📈 Time & Space Complexity:
# - set(): O(1) — append to list
# - get(): O(log n) — binary search on timestamps
# - Space: O(n) — for storing all (key → timestamps + values)

# 📝 My Takeaway:
# ✅ Using list-of-lists is powerful when index correlation matters
# ✅ Hashmap + sorted array + binary search = great combo for time/value-based lookups
# ✅ Think beyond just key-value → structure your value based on access pattern
