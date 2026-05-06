class TimeMap:

    def __init__(self):
        #{key :[timestamp, value]}のデータ型で管理
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] #valueはリストで作成。

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1

            else:
                right = mid - 1

        return res