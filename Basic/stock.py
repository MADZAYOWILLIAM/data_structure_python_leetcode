class Stock:
    """
    Stock Price Span Calculator
    This class calculates the span of stock prices, where the span is defined as
    the maximum number of consecutive days just before the given day, where the
    price of the stock on the current day is less than or equal to its price on
    the given day.
    Uses a monotonic stack approach for efficient O(1) amortized time complexity
    per price query.
    Attributes:
        monotonic_stack (list): Stack of tuples containing (price, span) pairs,
                               maintained in increasing order of prices.
    Methods:
        next(price: int) -> int:
            Calculate the span for the given price.
            Args:
                price (int): The stock price for the current day.
            Returns:
                int: The span value (number of consecutive days with price <= current price).
            Time Complexity: O(1) amortized
            Space Complexity: O(n) where n is the number of prices processed
    """

    def __init__(self):
        self.monotonic_stack = []

    def next(self, price: int) -> int:
        current_span = 1
        while self.monotonic_stack and self.monotonic_stack[-1][0] <= price:
            current_span += self.monotonic_stack.pop()[1]
        self.monotonic_stack.append((price, current_span))
        return current_span


# Your Stock object will be instantiated and called as such:
Stock().next(100)
Stock().next(80)
Stock().next(60)
Stock().next(70)
Stock().next(60)
Stock().next(75)
Stock().next(85)
