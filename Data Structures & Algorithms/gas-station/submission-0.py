class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        current = 0
        total = 0
        n = len(gas)

        while current <= 2*n - 1:
            total += gas[current % n] - cost[current % n]
            current += 1
            if total < 0:
                start = current % n
                total = 0
            elif start == current % n:
                return start
        return -1