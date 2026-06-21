class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        stack = []
        res = 0
        for pos, speed in cars:
            time = (target - pos) / speed
            if not stack:
                stack.append(time)
                res += 1
            if stack and time > stack[-1]:
                stack.pop()
                stack.append(time)
                res += 1
        return res
