import importlib.util
import sys

def load_module_from_path(path):
    module_name = "mymodule"  # Assign a name to the module

    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


if __name__ == '__main__':
    filename=sys.argv[1]


    module = load_module_from_path(filename)
    if hasattr(module, 'line'):
        for t in sys.stdin:
            module.line(t)
    if hasattr(module, 'end'):
        module.end()

