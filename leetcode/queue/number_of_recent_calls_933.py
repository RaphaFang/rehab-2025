from collections import deque
class RecentCounter:
    # ! 題目真正要問的是多次計算後，這個list其實不用存放這麼多資料，這時要怎麼丟垃圾？
    # 不必紀錄完整的list，而是超過3000的資料就丟棄
    # ------------------------------------------
    # 33ms
    # ! 兩者差異在於deque可以更快的迭代list，而pop需要把東西全部搬移
    def __init__(self):
        self.start = deque
        # self.start = []

    def ping(self, t:int) -> int:
        self.start.append(t)
        while self.start[0] <t-3000:
            self.start.popleft()
        return len(self.start)
    

    # ------------------------------------------
    # 46ms
    def ping(self, t: int) -> int:
        self.start.append(t)
        while self.start[0] < t - 3000:
            self.start.pop(0)
        return len(self.start)

    # ------------------------------------------
    # ! 這邊for會變慢，原因不是因為for不好，而是我查找對象list，會讓重新呼叫時，每次都重新跑完整的list
    def ping(self, t: int) -> int:
        self.start.append(t)
        t_index = len(self.start) - 1
        # t_index = self.start.index(t)

        temp_index = 0
        for i,n in enumerate(self.start):
            if n >= t - 3000:
                temp_index = i
                return t_index-temp_index+1
    # ! 不要用index()，他會是O(n)，如果能用其他方式會更快，例如我這邊用len() 會是 O(1)
    # ! 不要再loop中用index()
        
    # ------------------------------------------
    # 這絕對是效率最差的作法，

    # def ping(self, t: int) -> int:
    #     self.start.append(t)
    #     counter = 0
    #     for n in self.start:
    #         if n >= t-3000+1 and n<=t:
    #             counter+=1
    #     return counter

        


# obj = RecentCounter()
# param_1 = obj.ping(t)

