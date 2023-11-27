import pandas as pd
acc = []
def many(xs):
    data = [ t.strip().split("\t") for t in xs]
    print(len(data))
    acc.append(pd.DataFrame(data))

def end():
    print(pd.concat(acc))




