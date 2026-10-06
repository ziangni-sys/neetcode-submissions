class StockSpanner:

    def __init__(self):
        self.stack = []
        #(days, k)
    def next(self, price: int) -> int:
        stack = self.stack
        days = 1
        while stack and stack[-1][1] <= price:
            k,_ = stack.pop()
            days += k
        stack.append((days,price))
        return days
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)