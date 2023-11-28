import numpy as np
from types import SimpleNamespace
acc = SimpleNamespace(value=0)

# magic name
def many(xs):
  v = np.array(xs).astype(int)
  acc.value += np.sum(v)

def end():
  print(acc.value)
