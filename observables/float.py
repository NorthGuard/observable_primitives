from observable_primitives.observables.numeric_base import ObservableNumeric


class ObservableFloat(ObservableNumeric):
    def __init__(self, val=0.0):
        """
        A float which is observable.
        All methods and operations that work on a float should work on this class and have identical behavior.
        The only exception are the augmented arithmetic assignments, these all call the observers:
            +=, -=, *=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=
        :param val: Anything that can be cast to a float.
        """
        super().__init__(float(val))

    # Arithmetics

    def __pow__(self, power, modulo=None):
        return pow(self._val, power, modulo)

    # Arithmetics: Divisions and Modulo

    def __floordiv__(self, other):
        return self._val // other

    def __mod__(self, other):
        return self._val % other

    def __divmod__(self, other):
        return self._val // other, self._val % other

    # Conversions

    def __complex__(self):
        return complex(self._val)

    def __int__(self):
        return int(self._val)

    def __float__(self):
        return float(self._val)

    def __round__(self, n=None):
        return round(self._val, n)

    # Augmented arithmetics

    def __imod__(self, other):
        previous = self._val
        self._val %= other
        return self._ireturn(method="__imod__", other=other, previous=previous)

    def __ipow__(self, other, modulo=None):
        previous = self._val
        self._val = pow(self._val, other, modulo)
        return self._ireturn(method="__ipow__", other=other, modulo=modulo, previous=previous)

    def __ilshift__(self, other):
        previous = self._val
        self._val <<= other
        return self._ireturn(method="__ilshift__", other=other, previous=previous)

    def __irshift__(self, other):
        previous = self._val
        self._val >>= other
        return self._ireturn(method="__irshift__", other=other, previous=previous)

    def __iand__(self, other):
        previous = self._val
        self._val &= other
        return self._ireturn(method="__iand__", other=other, previous=previous)

    def __ixor__(self, other):
        previous = self._val
        self._val ^= other
        return self._ireturn(method="__ixor__", other=other, previous=previous)

    def __ior__(self, other):
        previous = self._val
        self._val |= other
        return self._ireturn(method="__ior__", other=other, previous=previous)

    # Observation method

    def _ireturn(self, *, method, other, **kwargs):
        # Check if incorrect type
        if not isinstance(self._val, float):
            self._val = float(self._val)

        # Notify observers
        self.update_observers(method=method, other=other, new_val=self._val, **kwargs)

        return self

    # Class specifics
    @property
    def imag(self):
        return 0

    @property
    def real(self):
        return self._val

    def conjugate(self):
        return complex(self._val, 0)

    def as_integer_ratio(self):
        return self._val.as_integer_ratio()

    def hex(self):
        return self._val.hex()

    def fromhex(self, s):
        return self._val.fromhex(s=s)

    def is_integer(self):
        return self._val.is_integer()
