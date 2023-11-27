# implicit begin
acc = 0

def one(x):
    global acc
    acc += len(x.split(' '))

def end():
    print(acc)
