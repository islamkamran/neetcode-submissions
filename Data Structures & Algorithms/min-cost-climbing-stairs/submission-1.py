class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # cost = [10,15,20]

        cost.append(0)
        # now cost is cost = [10,15,20,0]

        # from 0 to reach 0 it take zero cost so append 0
        # from 20 to reach 0 it takes 20 cost so two skip
        # from 15 to reach 0 in 1 step it will take 15 + 20 = 35
        # from 15 to reach 0 in 2 step it will take 15
        # from 10 to reach 0 in 1 step = 10 + 15 + 20 = 45
        # from 10 to reach 0 in 2 step = 10 + 20 = 30

        # so our goal is now to put the above logic in code and use the same array for putting the cost instead of its orignal value as at the end cost matters so as mentioned we can start from 0 or 1 so min of 0 and 1 is the result
        for i in range(len(cost)-3, -1,-1):
            # as we can take one or two step so whatever is the minimum of those take that when taking step have to consider its own cost
            # cost[i] = min(cost[i] + cost[i+1], cost[i]+ cost[i+2])
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
        