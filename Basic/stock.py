class Stock:
    def __init__(self):
        self.monotonic_stack=[]

    def next(self, price: int) -> int:
        current_span=1
        while self.monotonic_stack and self.monotonic_stack[-1][0]<=price:
            current_span+=self.monotonic_stack.pop()
        self.monotonic_stack.append((price,current_span))
        return current_span
    
# Your Stock object will be instantiated and called as such:
Stock().next(100)
Stock().next(80)
Stock().next(60)
Stock().next(70)
Stock().next(60)
Stock().next(75)
Stock().next(85)
   