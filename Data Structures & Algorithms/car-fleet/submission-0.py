class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] 
        time_pos = [( (target-position[i])/speed[i], position[i]) for i in range(len(speed)) ]
        time_pos.sort(key=lambda x: x[1])
        fleet = 0 
        while time_pos:
            time, i = time_pos.pop()
            fleet += 1
            while time_pos and  time >= time_pos[-1][0]:
                time_pos.pop()
        return fleet