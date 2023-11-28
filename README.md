# pyawk
Create AWK style scripts in python. Batch processing and batteries included. 

## Installation

```
# from github
pip install git+https://github.com/apetrov/pyawk.git@master

# from repo
git clone git@github.com:apetrov/pyawk.git && cd pyawk && make install
```

## Features
* Implicit script initialization similar to AWK BEGIN{}
* Explicit script finish, optional, similar to AWK END{}
* Process by line, similar to AWK {}
* Batch processing, receive an array of input strings instead of single string
* Compatible with UNIX pipe
* Designed to work with STDIN/STDOUT, no intention to support input from file.

## Usecase

```
seq 1 1000 | python -m pyawk sum.py
```

```sum.py
from types import SimpleNamespace

# there are other options of containers:
# acc = dict(value=0)
# acc = [0]
acc = SimpleNamespace(value=0)

# magic name, tells pyawk that it's one method call per line in STDIN
def one(x):
    acc.value+=int(x)

def end():
    print(acc.value)
```

which is equivalent of:

```
seq 1 1000 | awk -f sum.awk

or

seq 1 1000 | awk '{ acc += $0 } END { print acc }'
```

``` sum.awk
BEGIN {
    acc = 0
}

{
    acc += $0
}

END {
    print acc
}
```

### Batch mode
```
# process input in batch size of 1000
seq 1 100000 | python -m pyawk batch_sum.py -n 1000
```

```batch_sum.py
import numpy as np
from types import SimpleNamespace
acc = SimpleNamespace(value=0)

# magic name
def many(xs):
  v = np.array(xs).astype(int)
  acc.value += np.sum(v)

def end():
  print(acc.value)
```

## Performance
It's a zero-dependency project so it's startup time is negligible. 
```
echo 'foo' | time python -m pyawk test/empty.py
```

```
python -m pyawk test/empty.py  0.03s user 0.01s system 90% cpu 0.052 total
```

```test/empty.py
def one(x):
  pass
```

In terms of overall performance, i didn't benchmark it but it's comfortable at processing 50GB CSV file in batch size=100_000 mode.
pd.read_csv() has an order of magnitude higher impact on script run time comparing to reading from stdin.
