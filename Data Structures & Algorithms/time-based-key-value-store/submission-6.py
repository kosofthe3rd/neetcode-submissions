class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            self.store[key].append([timestamp, value])
        else:
            self.store[key].append([timestamp, value])
        self.store[key].sort(reverse = True)

    
    def get(self, key: str, timestamp: int) -> str:
        print(self.store)
        if key not in self.store:
            return ""
        else:
            for time, value in self.store[key]:
                if time <= timestamp:
                    return value
        return ""
        
