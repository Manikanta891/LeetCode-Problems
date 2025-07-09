class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        
        pivot=start

        def binary(start,end):
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return -1
        
        #Now we consider searching element in 1st half and the 2nd half individually
        result=binary(0,pivot-1)
        if result!=-1:
            return result
        
        return binary(pivot,len(nums)-1)


# 🚀 Problem Summary:
# Given: A rotated sorted array `nums` (without duplicates) and a `target` value
# Goal: Return the index of `target` in the array, or -1 if not found

# 🧩 Brute Force Idea:
# Do a linear search over the array and check each element
# Time: O(n)
# Space: O(1)
# Not optimal for large inputs

# ⚡ Optimization / Pattern Used:
# Pattern: Pivot-based Binary Search
# Step 1: Find the pivot — the index of the smallest element (where rotation happened)
#         → If `nums[mid] > nums[end]`, pivot is to the right
#         → Else, pivot is to the left
# Step 2: Once pivot is found, do binary search in:
#         → Left part [0 to pivot - 1]
#         → Right part [pivot to end]
# Why this works? — Because the array is sorted in both halves, binary search is valid in each

# 🔑 Key Insight:
# The rotated array can be split into two sorted halves
# Once pivot is found, just perform standard binary search in the correct sorted segment

# 🧠 Why it works:
# Pivot finding uses modified binary search to find smallest element
# Then binary search guarantees O(log n) lookup in sorted segments
# Separating pivot search and value search makes logic simpler

# 📈 Time & Space Complexity:
# Time: O(log n) — pivot search + binary search
# Space: O(1) — no extra memory used

# 📝 My Takeaway:
# This problem is a **foundational binary search twist**:
#   - Think "where does sortedness break?"
#   - Use modified binary logic to locate the inflection point
# Practice variant: Search with **duplicates allowed** (needs extra condition handling)
