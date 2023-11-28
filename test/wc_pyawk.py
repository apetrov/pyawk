# implicit begin
from types import SimpleNamespace
state = SimpleNamespace(acc=0)

def one(x):
    state.acc += len(x.split(' '))

def end():
    print(state.acc)
