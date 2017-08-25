from observable_primitives.base import Observer


class NumericPrintObserver(Observer):
    def _observation_string(self, *args, **kwargs):
        return f"{type(self).__name__}({kwargs['previous']} {kwargs['method']} {kwargs['other']} = {kwargs['new_val']})"

    def observe(self, *args, **kwargs):
        print(self._observation_string(*args, **kwargs))


class HoldNumericPrintObserver(NumericPrintObserver):
    def __init__(self, observables=None):
        super().__init__(observables=observables)
        self._observations = []

    def observe(self, *args, **kwargs):
        self._observations.append(self._observation_string(*args, **kwargs))

    def print(self, indent=None):
        indent = "" if indent is None else indent
        self._observations.reverse()
        while self._observations:
            item = self._observations.pop()
            indent = indent if isinstance(indent, str) else " " * indent
            print(indent + item)


class PrintObserver(Observer):
    def observe(self, *args, **kwargs):
        if kwargs:
            kwargs = f"{kwargs}"[1:-1]
        else:
            kwargs = ""
        if args:
            args = f"{args}"[1:-1]
        else:
            args = ""

        if args and kwargs:
            print(f"Observed({args}, {kwargs})")
        elif args:
            print(f"Observed({args})")
        elif kwargs:
            print(f"Observed({kwargs})")
        else:
            print(f"Observed()")