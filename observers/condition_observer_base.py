from observable_primitives.base import Observer, Observable


class ConditionObserver(Observer, Observable):
    def __init__(self, name=None, default=False, observables=None):
        Observer.__init__(self, observables=observables)
        Observable.__init__(self)
        self._status = default
        self._reason = None
        self._name = name

    def _update_status(self, *args, **kwargs):
        raise NotImplementedError

    @property
    def name(self):
        return self._name

    @property
    def status(self):
        return self._status

    @property
    def reason(self):
        return self._reason

    def __bool__(self):
        return self._status

    def __and__(self, other):
        return MultiConditionObserver(observable1=self, observable2=other, operator="and")

    def __or__(self, other):
        return MultiConditionObserver(observable1=self, observable2=other, operator="or")

    def observe(self, *args, **kwargs):
        self._update_status(*args, **kwargs)
        self.update_observers(obj=self, status=self._status, reason=self._reason)

    def report(self):
        str1 = f"{self.name}({{}})" if self.name is not None else "{}"
        str2 = f"{self.status} ; {self.reason}" if self.status else "False"
        return str1.format(str2)

    def _relevant_settings_names(self):
        raise NotImplementedError

    def __str__(self):
        return self.describe()

    def __repr__(self):
        return str(self)

    def describe(self):
        names = self._relevant_settings_names()  # list[str]

        string = []
        for name in names:
            val = getattr(self, name)
            string.append(f"{name.strip('_')}={val}")

        name_string = "" if self.name is None else f"'{self.name}', "
        if name_string == "":
            name_string = "Never"
        string = type(self).__name__ + "(" + name_string + ", ".join(string) + ")"
        return string


class MultiConditionObserver(ConditionObserver):
    def __init__(self, observable1, observable2, operator, name=None):
        super().__init__(name=name, observables=[observable1, observable2])

        # Note observables
        self._observable1 = observable1  # type: ConditionObserver
        self._observable2 = observable2  # type: ConditionObserver
        self._operator = operator

    def __add__(self, other):
        if not isinstance(other, str):
            raise ValueError(f"Only a string can be added to {type(self).__name__} (sets the name).")
        self._name = other
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def _relevant_settings_names(self):
        raise NotImplementedError

    def describe(self):
        name_string = "" if self.name is None else f"'{self.name}'"
        str1 = type(self).__name__ + "(" + name_string + ", {})"
        str2 = f"{self._observable1.describe()} {self._operator} {self._observable2.describe()}"
        return str1.format(str2)

    def _update_status(self, *args, **kwargs):
        if self._operator == "and":
            self._status = bool(self._observable1) and bool(self._observable2)
            if self.status:
                self._reason = f"({self._observable1.report()}) and ({self._observable2.report()})"
            else:
                self._reason = None
        elif self._operator == "or":
            self._status = bool(self._observable1) or bool(self._observable2)
            if self.status:
                self._reason = f"({self._observable1.report()}) or ({self._observable2.report()})"
            else:
                self._reason = None
