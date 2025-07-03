class Solution:
    def subsets(self, nums):
        res=[]
        subarray=[]
        def helper(index):
            if index==len(nums):
                res.append(subarray[:])
                return 
            subarray.append(nums[index])
            helper(index+1)
            subarray.pop()
            helper(index+1)
        helper(0)
        return res
    

# 🚀 Problem Summary:
# Given: A list of integers `nums`
# Goal: Return all possible subsets (the power set) of the input list

# 🧩 Brute Force Idea:
# Generate all combinations by checking all binary representations of 2^n combinations
# For each bitmask of size n, build subset from `nums`
# Time: O(n * 2^n) — still acceptable, but less intuitive than recursion
# Space: O(2^n) — total number of subsets

# ⚡ Optimization / Pattern Used:
# Pattern: Backtracking
# Recursively explore two choices at each index:
#   - Include the current element in the subset
#   - Exclude the current element
# Use a helper function with an index to decide which elements to consider
# Why needed? → Generates all subsets in a tree-like recursive fashion

# 🔑 Key Insight:
# At every index, you branch into two paths — include or exclude
# Base case: if index == len(nums), you've built a complete subset → add to result

# 🧠 Why it works:
# The recursion tree has 2^n leaves, each representing a valid subset
# Using `subarray[:]` ensures we're appending a copy of the current subset (not a reference)

# 📈 Time & Space Complexity:
# Time: O(n * 2^n) — 2^n subsets, each may take up to O(n) to copy
# Space: O(n) — recursion stack and subset building

# 📝 My Takeaway:
# This is one of the cleanest examples of backtracking
# Great for practicing decision trees: include vs exclude
# Variants include: Subsets with Duplicates, K-sized subsets, etc.




# # Understanding Subsets with Backtracking: A Magical Backpack Adventure
# ## 🎒 The Magical Backpack Adventure (Story to Understand Subsets)

# ### 📍 The Setup

# You're on a magical quest. 🧙‍♂️ You're standing in front of a trail of **treasure items** — say they are `[Sword, Potion, Shield]`. Your mission?

# > Try out **every possible combination** of items to carry in your magical backpack. Some combos may be strong, some weak — but you want to **test them all** before heading into battle.

# ---

# ## 🪜 The Decision Path (How Backtracking Works Here)

# At each item, you’re faced with a **magical talking signpost**:

# > ❓ *"Do you want to pick up this item or leave it behind?"*

# You answer that question **for every item** one-by-one, going forward on the trail.

# So at every stop:

# * ✅ Take the item → move to next with it in your bag
# * ❌ Skip the item → move to next without it

# And this keeps branching, like a decision tree.

# ---

# ## 🧠 Let’s Walk Through It — Step by Step

# Your trail: `[Sword, Potion, Shield]`
# Backpack starts empty: `[]`

# ---

# ### 🔁 Step-by-Step Adventure

# 1. **At Sword**

#    * ✅ Take it → Backpack: `[Sword]`

#      * **At Potion**

#        * ✅ Take it → Backpack: `[Sword, Potion]`

#          * **At Shield**

#            * ✅ Take it → `[Sword, Potion, Shield]` ✅ (record this)
#            * ❌ Skip it → `[Sword, Potion]` ✅
#        * ❌ Skip Potion → Backpack: `[Sword]`

#          * **At Shield**

#            * ✅ Take it → `[Sword, Shield]` ✅
#            * ❌ Skip it → `[Sword]` ✅
#    * ❌ Skip Sword → Backpack: `[]`

#      * **At Potion**

#        * ✅ Take it → `[Potion]`

#          * **At Shield**

#            * ✅ Take it → `[Potion, Shield]` ✅
#            * ❌ Skip it → `[Potion]` ✅
#        * ❌ Skip Potion → `[]`

#          * **At Shield**

#            * ✅ Take it → `[Shield]` ✅
#            * ❌ Skip it → `[]` ✅

# You’ve now explored **every possible subset**:

# ```
# [
#  [],
#  [Shield],
#  [Potion],
#  [Potion, Shield],
#  [Sword],
#  [Sword, Shield],
#  [Sword, Potion],
#  [Sword, Potion, Shield]
# ]
# ```

# > Each decision you made was a **binary yes/no**, and you explored all possible outcomes using recursion + backtracking.

# ---

# ## 🔄 Why Backtrack?

# After trying one path (say, you took Sword and Potion), you **remove** the last item and try the path *without it*. That’s why we use:

# ```python
# subarray.pop()  # "Remove last item from the bag"
# ```

# It’s like undoing a decision and trying the alternative route.

# ---

# ## 📦 So, What’s the TL;DR?

# * Think of each number/item as a **yes/no decision point**
# * Use **recursion** to explore both choices
# * Use **backtracking** to undo decisions and explore the next option
# * You’ll end up covering **every possible combination** of items

# ---

# ## 🚀 Remember It This Way:

# > “Every subset is a different version of your backpack on the journey — you either picked up that item or you didn’t. Backtracking lets you try *every possible adventure*.”

# Now, the next time you see this code, you won’t just understand it — you’ll *feel like you’re back on the trail*, making decisions with your magical backpack. 🧙‍♂️🎒


