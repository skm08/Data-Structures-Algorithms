class ProductOfNumbers:
    def __init__(self):
        self.stream = [1]
        self.n = 1
        self.last_zero_idx = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero_idx = self.n

        if self.stream[-1] == 0:
            self.stream.append(num)
        else:
            self.stream.append(self.stream[-1] * num)
        self.n += 1

    def getProduct(self, k: int) -> int:
        if self.last_zero_idx >= self.n - k:
            return 0
        if self.stream[self.n - k - 1] == 0:
            return self.stream[self.n - 1]
        else:
            return self.stream[self.n - 1] // self.stream[self.n - k - 1]