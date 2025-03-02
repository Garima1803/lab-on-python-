class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse('giraffe')
for char in rev:
    print(char)
 # Outputs: e, f, a, r, g
print("program by Diya Bhutani- 0221BCA041")



