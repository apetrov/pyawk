# implicit begin
acc = 0

def line(x):
    global acc
    acc += len(x.split(' '))

def end():
    print(acc)
