import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        state = [(x, v) for x, v in zip(position, speed)]
        state.sort(key = lambda x : x[0] , reverse = True)
        durations = [(target - x)/v for x, v in state]
        
        fleets = []
        for duration in durations:
            if fleets and fleets[-1] >= duration:
                continue;
            else:
                fleets.append(duration)
        return len(fleets)