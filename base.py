
class Observable:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def unregister_all(self):
        if self._observers:
            del self._observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self._observers:  # type: Observer
            observer.observe(*args, **kwargs)


class Observer:
    def __init__(self, observables=None):
        if observables is not None:

            if isinstance(observables, Observable):
                observables.register(self)
            elif isinstance(observables, list):
                for observable in observables:
                    observable.register(self)
            else:
                raise ValueError(f"Incorrect values passed to Observer argument observables ({type(observables)}).")

    def observe(self, *args, **kwargs):
        raise NotImplementedError
