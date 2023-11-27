
class State:
    def __init__(self):
        self.reset()

    def reset(self):
        self.acc = []
        self.n = 0

    def accept(self, x):
        self.acc.append(x)
        self.n+=1

acc = State()

def line(x):
    acc.accept(x)
    if acc.n == 1000:
        print("batch!")
        acc.reset()


def end():
    print(acc.n)

