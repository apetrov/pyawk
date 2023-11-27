import importlib.util
import argparse
import sys

def load_module_from_path(path):
    module_name = "mymodule"  # Assign a name to the module

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def create_args():
    parser = argparse.ArgumentParser(description="STDIN python tool")
    parser.add_argument('file', type=str, help='python file to run')
    parser.add_argument('-n', '--number', type=int, default=1, help='Batch size')

    args = parser.parse_args()
    return args


class Runner:
    def __init__(self, module, runner):
        self.module = module
        self.runner = runner

    def run(self, io):
        self.runner.run(io)

    def end(self):
        if hasattr(self.module, 'end'):
            self.module.end()

class One:
    def __init__(self, module):
        self.module = module

    def run(self, io):
        module = self.module
        for t in io:
            module.one(t)

class Many:
    def __init__(self, module, n) :
        self.module = module
        self.n = n

    def run(self, io):
        pass

class Null:
    def run(self, io):
        pass

def create_executor(module, n):
    if hasattr(module, 'one'):
        return One(module)
    if hasattr(module, 'many'):
        return Many(module, n)
    return Null()

def main():
    args = create_args()
    module = load_module_from_path(args.file)
    executor = create_executor(module, args.number)
    runner = Runner(module, executor)
    runner.run(sys.stdin)
    runner.end()

if __name__ == '__main__':
    main()
