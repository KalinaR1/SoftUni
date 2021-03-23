from collections import deque


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = deque(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        for i in range(len(self.sequence)):
            self.number -= 1
            value = self.sequence.popleft()
            self.sequence.append(value)
            return value


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')
