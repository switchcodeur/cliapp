from sys import argv
from typing import Tuple
from types import FunctionType


class CliApp:
    def __init__(self) -> None:
        self.functions = {}
    
    def add_flag(self, name: str, fn: FunctionType) -> None:
        if len(name) == 1:
            name = "-" + name
        else:
            name = "--" + name

        if not self.functions.get(name):
            self.functions[name] = []

        self.functions[name].append(fn)

    
    def flag(self, name: str, *aliases: Tuple[str]) -> FunctionType:
        def decorator(fn: FunctionType) -> FunctionType:
            self.add_flag(name, fn)
            for alias in aliases:
                self.add_flag(alias, fn)

            def wrapper(*args, **kwargs) -> None:
                fn(*args, **kwargs)

            return wrapper
        
        return decorator

    def run(self) -> None:
        functions = []

        for index, flag in enumerate(argv):
            if flag in self.functions:
                functions.append([flag, []])

                index += 1
                while index < len(argv) and not argv[index] in self.functions:
                    index += 1
                    functions[-1][1].append(argv[index - 1])
        
        for flag in functions:
            for function in self.functions[flag[0]]:
                function(*flag[1])
                