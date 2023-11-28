import io
import csv
import pandas as pd

acc = []
def many(xs):
    def parse_line(x):
        return next(csv.reader(io.StringIO(x)))
    data = [ parse_line(t) for t in xs]
    acc.append(pd.DataFrame(data))

def end():
    print(pd.concat(acc).shape)




