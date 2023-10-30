from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #        Time each car needs to reach the target (sorted by position)
        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_speed.sort(reverse=True, key=lambda x: x[0])
        stack = []

        for pos, speed in pos_speed:
            time = (target - pos) / speed
            if stack and stack[-1] >= time:
                time = stack.pop()
            stack.append(time)
        return len(stack)


s = Solution()
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(s.carFleet(target, position, speed))
