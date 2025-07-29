# Problem:
# You are given an array `cost` where `cost[i]` is the cost of `i-th` step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from step 0 or step 1.
# Return the minimum cost to reach the top of the floor (beyond the last step).

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append 0 to represent the top of the floor
        cost.append(0)

        # Start filling from the end towards the beginning
        for i in range(len(cost) - 3, -1, -1):
            # Add to current cost the minimum cost from the next two possible steps
            cost[i] += min(cost[i + 1], cost[i + 2])

        # Return the minimum of starting from step 0 or step 1
        return min(cost[0], cost[1])
