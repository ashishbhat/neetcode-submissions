class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        stairs = len(cost)
        min_cost = [0]*(stairs)
        min_cost[0] = 0
        min_cost[0] = 0

        for stair in range(2, stairs):
            min_cost[stair] = min(
                min_cost[stair-1]+cost[stair-1],
                min_cost[stair - 2]+cost[stair-2]
            )
        return min(min_cost[-1]+cost[-1], min_cost[-2]+cost[-2])

