class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self.n = 0


    def __str__(self):
        if self.n > 0:
            return (self.n * "🍪")
        else:
            return ""


    def deposit(self, n):
        if n < 0:
            raise ValueError("Deposit amount cannot be negative")
        elif self.n + n > self._pcapacity:
            raise ValueError("Jar is full")
        else:
            self.n += n


    def withdraw(self, n):
        if n < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        elif self.n - n < 0:
            raise ValueError("Not enough cookies in the jar")
        else:
            self.n -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self.n
