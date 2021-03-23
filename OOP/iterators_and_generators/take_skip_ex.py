class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.value = 0
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.i:
            raise StopIteration
        value = self.value
        self.value += self.step
        self.i += 1
        return value


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
