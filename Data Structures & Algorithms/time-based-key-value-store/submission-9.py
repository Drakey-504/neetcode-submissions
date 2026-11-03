class TimeMap:

    def __init__(self):
        self.lookup = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookup[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        key_list = self.lookup[key]

        if len(key_list) == 0:
            return ""

        l, r = 0, len(key_list) - 1
        res_index = 0

        while l <= r:
            mid = l + (r-l)//2
            if key_list[mid][0] == timestamp:
                return key_list[mid][1]
            elif key_list[mid][0] < timestamp:  
                res_index = max(res_index, mid)
                l = mid+1
            else:
                r = mid-1

        if key_list[res_index][0] <= timestamp:
            return key_list[res_index][1]                    
        else:
            return ""
