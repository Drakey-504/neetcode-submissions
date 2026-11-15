class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = []
        
        for i in range(len(position)):
            time.append ((position[i], ((target-position[i])/ speed[i]))) 

        time = sorted(time,  key=lambda p:p[0], reverse = True)  
        fleet_stack = []
        res = 0

        for c in time:

            if fleet_stack and c[1] > fleet_stack[-1]:
                while fleet_stack and c[1] > fleet_stack[-1]:
                    fleet_stack.pop()
                res += 1    

            fleet_stack.append(fleet_stack[-1] if fleet_stack else c[1])

        if fleet_stack:
            res += 1

        return res        
