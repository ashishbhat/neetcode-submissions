import heapq
class MedianFinder:

    def __init__(self):
        self.medians = []
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not type(num) is int:
            return
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if len(self.right) - len(self.left) > 1:
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -temp)
        
        if len(self.left) - len(self.right) > 1:
            temp = -heapq.heappop(self.left)
            heapq.heappush(self.right, temp)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            res = (-self.left[0] + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            res = float(-self.left[0])
        else:
            res = float(self.right[0])
        return res