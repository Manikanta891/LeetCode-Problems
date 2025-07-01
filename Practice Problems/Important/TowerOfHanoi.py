def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


N = 3

TowerOfHanoi(N, 'A', 'C', 'B')

#The main task is given recursively the big step to another recursion function then it will continuosly break down into small tasks
#Before moving n disks we need to move remaining n-1 disks
#Before moving n-1 disks we need to move n-2 disks 
# 🔺 The Basic Setup

# You have:

# * **3 rods** (let’s call them A, B, and C)
# * **N disks** of different sizes stacked on rod A, **largest at the bottom, smallest on top**
# * Goal: Move the entire stack from **rod A to rod C**, **one disk at a time**

# ---

# ### ✅ The Rules

# 1. **Only one disk can be moved at a time**
# 2. **You can only move the top disk** from any rod
# 3. **A larger disk can never be placed on a smaller one**

# ---

# ### 🧠 The Core Logic (Recursive Thinking)

# If you try to solve it manually with, say, 4 or 5 disks, you’ll notice a pattern—but your brain might melt trying to do it efficiently. That’s where **recursion** comes in.

# #### 🧩 Here's the idea:

# To move `n` disks from rod A to rod C using rod B as auxiliary:

# 1. **Move (n-1) disks** from A to B, using C as temporary storage
# 2. **Move the largest disk** (disk `n`) from A to C
# 3. **Move the (n-1) disks** from B to C, using A as temporary

# And this just keeps going until you’re down to a single disk—**the base case**.

# ---

# ### 🔄 Recursion in Action (With 3 Disks)

# Let’s walk it through:

# 1. Move disk 1 from A to C
# 2. Move disk 2 from A to B
# 3. Move disk 1 from C to B
# 4. Move disk 3 from A to C
# 5. Move disk 1 from B to A
# 6. Move disk 2 from B to C
# 7. Move disk 1 from A to C

# Boom. Done.

# ---

# ### 🧮 Minimum Moves Formula

# For `n` disks, minimum number of moves required is:

# So:

# * 3 disks → 7 moves
# * 4 disks → 15 moves
# * 10 disks → 1023 moves 😳

# ---

# ### 🤯 What's the Real Magic?

# The beauty is in the **recursive breakdown**. You’re not solving the whole problem at once—you’re trusting that the smaller problem will get handled the same way, just with fewer disks.

# It’s like telling a younger version of yourself:

# > "Hey, just do this little part, and I’ll take it from there."

# ---

# ### 💡 Why It Matters (Beyond Puzzles)

# Towers of Hanoi teaches:

# * **Recursive thinking** (a must for algorithms & problem-solving)
# * **Breaking big problems into smaller, solvable chunks**
# * Mental discipline to follow strict rules within constraints

# Perfect for algorithm design, backtracking problems, and even understanding stack-based recursion in languages like Python, C++, or Java.