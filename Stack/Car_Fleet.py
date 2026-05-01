class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #位置と速度をペアにし、ゴールに近い順にソート
        cars = sorted(zip(position, speed), reverse = True)

        stack = []
        for p, s in cars:
            arrival_time = (target - p) / s
            stack.append(arrival_time)
            #後ろの車が追い付くなら、一つの自動車群になる
            if len(stack) >= 2 and stack [-1] <= stack[-2]:
                stack.pop()

        return len(stack)