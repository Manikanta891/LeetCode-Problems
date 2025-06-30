class Solution:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        
        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets

#The above version is simple to read

#The below version is uses the same logic to store the time of cars
#Logic is simple car speed and position is make into tuple of individual unit
#Now they are sorted based on the position 
#Now according to problem the speed of nearest car is consider first
#If the cars far from target is takes less timev then previous car which is nearer to target 
#then there is fleet occur
#Other wise cars cannot undergoes fleet

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p, s) for p, s in zip(position, speed)]
#         pair.sort(reverse=True)
#         stack = []
#         for p, s in pair:  # Reverse Sorted Order
#             stack.append((target - p) / s)
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)



# 🚀 Problem Summary:
# Given: 
#   - target: final destination
#   - position[]: positions of cars (not necessarily sorted)
#   - speed[]: speed of each car
# Goal: Return the number of car fleets that will arrive at the destination
# Rule: If a car catches up to another before the destination, they form a fleet and move together

# 🧩 Brute Force Idea:
# Try to simulate motion for every car and check which ones collide
# Track each car's position at every time step — compare with others
# Time: O(n^2) or worse
# Space: O(n) — for storing states

# ⚡ Optimization / Pattern Used:
# Pattern: Greedy + Sort + Stack
# Step-by-step:
#   1. Pair each car’s position and speed: (pos, speed)
#   2. Sort cars by starting position in descending order (closer to target comes last)
#   3. Calculate time each car takes to reach target: (target - pos) / speed
#   4. If a car behind takes more time than the one ahead, it forms a **new fleet**
#   5. If it takes less or equal time, it merges into the fleet ahead

# 🔑 Key Insight:
# Time to reach the target determines whether a car catches up or not
# Cars can never pass each other — so once a slower car is ahead, everyone behind is stuck unless they’re slower

# 🧠 Why it works:
# By processing from nearest to farthest, we can simulate catch-ups using a stack or greedy pointer
# Only when a car behind takes longer, a new fleet is formed

# 📈 Time & Space Complexity:
# Time: O(n log n) — sorting the cars by position
# Space: O(n) — to store the fleet times or stack

# 📝 My Takeaway:
# Car Fleet is all about understanding "arrival time"
# Visualizing the movement and who catches whom helps
# This is a great greedy + sorting problem where reverse thinking (process from end) is key
