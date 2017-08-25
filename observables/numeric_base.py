from observable_primitives.base import Observable


class ObservableNumeric(Observable):
    def __init__(self, val):
        super().__init__()
        self._val = val

    @property
    def val(self):
        return self._val

    # Numerical comparisons

    def __lt__(self, other):
        return self._val < other

    def __le__(self, other):
        return self._val <= other

    def __eq__(self, other):
        return self._val == other

    def __ne__(self, other):
        return self._val != other

    def __ge__(self, other):
        return self._val >= other

    def __gt__(self, other):
        return self._val > other

    # Unary

    def __neg__(self):
        return -self._val

    def __pos__(self):
        return +self._val

    def __abs__(self):
        return abs(self._val)

    # def __invert__(self):
    #     return ~self._val

    # Arithmetics

    def __add__(self, other):
        return self._val + other

    def __radd__(self, other):
        return other + self._val

    def __sub__(self, other):
        return self._val - other

    def __rsub__(self, other):
        return other - self._val

    def __mul__(self, other):
        return self._val * other

    def __rmul__(self, other):
        return other * self._val

    # def __matmul__(self, other):
    #     return self._val @ other
    #
    # def __rmatmul__(self, other):
    #     return other @ self._val

    # def __pow__(self, power, modulo=None):
    #     return pow(self._val, power, modulo)
    #
    # def __rpow__(self, power, modulo=None):
    #     return pow(power, self._val, modulo)

    # Arithmetics: Divisions and Modulo

    def __truediv__(self, other):
        return self._val / other

    def __rtruediv__(self, other):
        return other / self._val

    # def __floordiv__(self, other):
    #     return self._val // other
    #
    # def __rfloordiv__(self, other):
    #     return other // self._val
    #
    # def __mod__(self, other):
    #     return self._val % other
    #
    # def __rmod__(self, other):
    #     return other % self._val
    #
    # def __divmod__(self, other):
    #     return divmod(self._val, other)
    #
    # def __rdivmod__(self, other):
    #     return divmod(other, self._val)

    # Arithmetics: Binary

    # def __lshift__(self, other):
    #     return self._val << other
    #
    # def __rlshift__(self, other):
    #     return other << self._val
    #
    # def __rshift__(self, other):
    #     return self._val >> other
    #
    # def __rrshift__(self, other):
    #     return other >> self._val

    # Boolean

    def __bool__(self):
        return bool(self._val)

    # def __and__(self, other):
    #     return self._val & other
    #
    # def __rand__(self, other):
    #     return other & self._val
    #
    # def __or__(self, other):
    #     return self._val | other
    #
    # def __ror__(self, other):
    #     return other | self._val
    #
    # def __xor__(self, other):
    #     return self._val ^ other
    #
    # def __rxor__(self, other):
    #     return other ^ self._val

    # Representation

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(repr(self))

    def __format__(self, format_spec):
        string = "{{:{}}}".format(format_spec)
        return string.format(self._val)

    # def __bytes__(self):
    #     return bytes(self._val)

    # Conversions

    # def __complex__(self):
    #     return complex(self._val)
    #
    # def __int__(self):
    #     return int(self._val)
    #
    # def __float__(self):
    #     return float(self._val)
    #
    # def __round__(self, n=None):
    #     return round(self._val, n)

    # Augmented arithmetics

    def __iadd__(self, other):
        previous = self._val
        self._val += other
        return self._ireturn(method="__iadd__", other=other, previous=previous)

    def __isub__(self, other):
        previous = self._val
        self._val -= other
        return self._ireturn(method="__isub__", other=other, previous=previous)

    def __imul__(self, other):
        previous = self._val
        self._val *= other
        return self._ireturn(method="__imul__", other=other, previous=previous)

    # def __imatmul__(self, other):
    #     previous = self._val
    #     self._val @= other
    #     return self._ireturn(method="__imatmul__", other=other, previous=previous)

    def __itruediv__(self, other):
        previous = self._val
        self._val /= other
        return self._ireturn(method="__itruediv__", other=other, previous=previous)

    def __ifloordiv__(self, other):
        previous = self._val
        self._val //= other
        return self._ireturn(method="__ifloordiv__", other=other, previous=previous)

    # def __imod__(self, other):
    #     previous = self._val
    #     self._val %= other
    #     return self._ireturn(method="__imod__", other=other, previous=previous)
    #
    # def __ipow__(self, other, modulo=None):
    #     previous = self._val
    #     self._val = pow(self._val, other, modulo)
    #     return self._ireturn(method="__ipow__", other=other, modulo=modulo, previous=previous)
    #
    # def __ilshift__(self, other):
    #     previous = self._val
    #     self._val <<= other
    #     return self._ireturn(method="__ilshift__", other=other, previous=previous)
    #
    # def __irshift__(self, other):
    #     previous = self._val
    #     self._val >>= other
    #     return self._ireturn(method="__irshift__", other=other, previous=previous)

    # def __iand__(self, other):
    #     previous = self._val
    #     self._val &= other
    #     return self._ireturn(method="__iand__", other=other, previous=previous)
    #
    # def __ixor__(self, other):
    #     previous = self._val
    #     self._val ^= other
    #     return self._ireturn(method="__ixor__", other=other, previous=previous)
    #
    # def __ior__(self, other):
    #     previous = self._val
    #     self._val |= other
    #     return self._ireturn(method="__ior__", other=other, previous=previous)

    # Observation method

    def _ireturn(self, *, method, other, **kwargs):
        raise NotImplementedError

    # Direct setter

    def set(self, val, method="set"):
        previous = self._val
        self._val = val
        return self._ireturn(method=method, other=val, previous=previous)
