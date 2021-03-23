class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        if not self.obj:
            raise StopIteration
        for key, value in self.obj.items():
            old_key = key
            old_value = value
            del self.obj[key]
            return old_key, old_value


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
