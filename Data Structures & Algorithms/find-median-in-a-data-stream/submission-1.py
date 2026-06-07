class MedianFinder:

    def __init__(self):
        self.order = []

    def addNum(self, num: int) -> None:
        i = 0
        while i < len(self.order) and self.order[i] < num:
            i += 1
        self.order.insert(i, num)
        

        # if not self.order:
        #     self.order.append(num)
        #     return
        # insert = 0
        # for i in range(len(self.order)):
        #     if self.order[i] == num:
        #         insert = i + 1
        #         self.order.insert(insert, num)
        #         return
        #     elif num > self.order[i]:
        #         insert = i + 1
        #     else:
        #         self.order.insert(insert, num)
        #         return
        # self.order.insert(insert, num)

    def findMedian(self) -> float:
        if len(self.order) % 2 == 1:
            return self.order[int(len(self.order) / 2)]
        else:
            smaller = self.order[int(len(self.order) / 2 - 1)]
            larger = self.order[int(len(self.order) / 2)]
            print(self.order)
            return (smaller + larger) / 2
        