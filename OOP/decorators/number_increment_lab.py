def number_increment(numbers):

    def increase():
        nonlocal numbers
        numbers = [numbers[i] + 1 for i in range(len(numbers))]
        return numbers

    return increase()

# def number_increment(numbers):
#
#     def increase():
#         for i in range(len(numbers)):
#             numbers[i] += 1
#         return numbers
#
#     return increase()

# print(number_increment([1, 2, 3]))