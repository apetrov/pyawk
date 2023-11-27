import sys

if __name__ == '__main__':
    filename=sys.argv[1]
    print(filename)
    with open(filename) as file:
        exec(file.read())

    begin()
    for t in sys.stdin:
        line(t)
    end()

