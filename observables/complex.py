from typing import SupportsComplex, SupportsAbs

from observable_primitives.observables.numeric_base import ObservableNumeric


class ObservableComplex(ObservableNumeric, SupportsComplex, SupportsAbs):
    def __init__(self, val):
        """
        A complex number which is observable.
        All methods and operations that work on complex should work on this class and have identical behavior.
        The only exception are the augmented arithmetic assignments, these all call the observers:
            +=, -=, *=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=
        :param complex val:
        """
        super().__init__(val)

    def __pow__(self, power):
        return self._val ** power

    def __rpow__(self, power):
        return power ** self._val

    def __complex__(self) -> complex:
        return self._val

    # Augmented arithmetics

    def __ipow__(self, other):
        previous = self._val
        self._val = self._val ** other
        return self._ireturn(method="__ipow__", other=other, modulo=None, previous=previous)

    # Observation method

    def _ireturn(self, *, method, other, **kwargs):
        # Check if incorrect type
        if not isinstance(self._val, complex):
            self._val = complex(self._val)

        # Notify observers
        self.update_observers(method=method, other=other, new_val=self._val, **kwargs)

        return self

    # Class specifics
    @property
    def imag(self):
        return self._val.imag

    @property
    def real(self):
        return self._val.real

    def conjugate(self):
        return self._val.conjugate()
