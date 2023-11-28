from types import SimpleNamespace

acc = SimpleNamespace(value=0)

def one(x):
    acc.value+=int(x)

def end():
    print(acc.value)


