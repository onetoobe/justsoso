
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
        yield b
for n in fab(5):
    print(n)

#
class Fab:
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration


    def __iter__(self):
        return self


# print(Fab(5))

for n in Fab(5):
    print(n)
#
#
# li=[1,2,3,4]
# it=iter(li)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# try:
#     next(it)
# except StopIteration:
#     pass




# for l in it:
#     print(l)




# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

