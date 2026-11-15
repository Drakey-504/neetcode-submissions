class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = []
        
        for i in range(len(position)):
            time.append ((position[i], ((target-position[i])/ speed[i]))) 

        time = sorted(time,  key=lambda p:p[0], reverse = True)  

        res = 1
        cur_fleet_time = time[0][1]

        i = 1
        while i < len(time):
            if time[i][1] > cur_fleet_time:
                cur_fleet_time =  time[i][1]
                res += 1
            i += 1    

        return res        
