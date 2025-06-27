class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n  # Final answer array
        stack = []  # Stores indices

        for i in range(n):
            # While current temp is higher than stack top's temp
            while stack and T[i] > T[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day  # Days waited
            stack.append(i)  # Push current day index

        return res
      
    


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res=[]
#         stack=[]
#         count=len(temperatures)-1   
        
#         for i in range(len(temperatures)-1,-1,-1):
#             stack.append(temperatures[i])
#             res.append(self.calculate(stack))
#             self.remove_ele(stack)
#         res.reverse()
#         return res
#     def calculate(self,stack):
#             count=0
#             for i in range(len(stack)-1,-1,-1):
#                 if stack[-1]<stack[i]:
#                     return count
#                 else:
#                     count+=1
#             else:
#                 return 0

#The below function not work because removing the elements will cause the count error
#     def remove_ele(self,stack):     
#         for ele in stack:
#             if stack[-1]>ele:
#                 stack.remove(ele)       
    
                
            
                
# 🚀 Problem Summary:
# Given: A list `T` of daily temperatures
# Goal: For each day, find how many days you'd have to wait until a warmer temperature
# If there is no future day with a warmer temperature, return 0 for that day

# 🧩 Brute Force Idea:
# For each day `i`, loop over every future day `j > i` and find the first `T[j] > T[i]`
# Count how many days it takes, or return 0 if none
# Time: O(n^2) — nested iteration
# Space: O(1) extra

# ⚡ Optimization / Pattern Used:
# Pattern: Monotonic Decreasing Stack
# Stack stores indices of days with unresolved warmer temperature
# For each day, while current temperature > stack top's temperature:
#     Pop and update result: `res[prev_day] = current_day - prev_day`
# Push current day index onto stack
# Why needed? → We only process each index once, maintaining order

# 🔑 Key Insight:
# Stack helps us "remember" unresolved indices and resolve them only when we find a warmer temperature
# It’s not about values — it’s about **waiting time**, which we compute using indices

# 🧠 Why it works:
# Stack maintains decreasing temperatures (top is the coldest unresolved)
# When a warmer day appears, we resolve all smaller temps before it
# Ensures each index is added and removed only once

# 📈 Time & Space Complexity:
# Time: O(n) — Each index is pushed and popped at most once
# Space: O(n) — For result array and stack

# 📝 My Takeaway:
# Monotonic stacks are powerful for "next greater element" types
# The key is to think in terms of indices, not just values
# Trying reverse iteration is good thinking — but forward stack logic fits cleaner here


