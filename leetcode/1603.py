"""
Runtime: 140 ms, faster than 67.89% of Python3 online submissions for Design Parking System.
Memory Usage: 14.9 MB, less than 25.92% of Python3 online submissions for Design Parking System.
"""
from collections import deque


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.lot = [0, 0, 0]
        self.cap = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        i = carType - 1
        spots_left = self.cap[i] - self.lot[i]
        if spots_left > 0:
            self.lot[i] += 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
