class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        k = self.keyStore.get(key)
        low = 0
        high = len(k)-1
        res = ""
        while(low<= high):
            m = (low+high)//2
            if k[m][1] <= timestamp:
                res = k[m][0]
                low = m + 1
            else:
                high = m - 1
        return res
        
