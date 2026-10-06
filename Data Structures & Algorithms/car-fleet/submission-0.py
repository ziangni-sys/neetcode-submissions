class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        f = len(cars)
        for car in cars:
            timeleft = (target - car[0]) / car[1]
            if not stack or stack[-1] < timeleft:
                stack.append(timeleft)
            else:
                f -= 1
        return f
