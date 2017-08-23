from observable_primitives.observers.condition_observer_base import ConditionObserver


class IntegerConditionObserver(ConditionObserver):
    def __init__(self, name=None, observable=None,
                 divisible_by=None,
                 if_less_than=None, if_more_than=None,
                 at_specific_value=None
                 ):
        """
        Watches an observable integer for various conditions.
        Silently keeps its internal status and provides it if needed.

        :param ObservableInteger observable: Observable integers to watch.
        :param int | list[int] divisible_by:
        :param int if_less_than:
        :param int if_more_than:
        :param int | list[int] at_specific_value:
        """
        super().__init__(name=name, default=False, observables=observable)
        self._divisible_by = divisible_by if (isinstance(divisible_by, list) or divisible_by is None) \
            else [divisible_by]
        self._if_less_than = if_less_than
        self._if_more_than = if_more_than
        self._at_specific_value = at_specific_value if isinstance(at_specific_value, list) \
            else [at_specific_value]
        self._observable = observable

        # Initialize
        self._initialize()

    def _initialize(self):
        self._update_status(new_val=self._observable.val, method="ObserverInitialize", other=None, previous=None)

    def _update_status(self, *, new_val, method, other, previous):
        # Specific iteration
        if self._at_specific_value is not None:
            if new_val in self._at_specific_value:
                self._reason = f"Specifically chosen value {new_val}"
                self._status = True
                return

        # Select iteration at specified iteration interval
        if self._divisible_by is not None:
            for div_val in self._divisible_by:
                if (new_val % div_val) == 0:
                    self._reason = f"Value {new_val} divisible by {div_val}"
                    self._status = True
                    return

        # Check for lower limit
        if self._if_less_than is not None and new_val < self._if_less_than:
            self._reason = f"Value {new_val} < {self._if_less_than}"
            self._status = True
            return

        # Check for upper limit
        if self._if_more_than is not None and new_val > self._if_more_than:
            self._reason = f"Value {new_val} > {self._if_more_than}"
            self._status = True
            return

        # Don't select iteration
        self._reason = None
        self._status = False


class CounterConditionObserver(IntegerConditionObserver):
    def __init__(self, name=None, observable=None,
                 at_every=None, at_relative=None,
                 if_first_count=False, if_last_count=None,
                 if_less_than=None, if_more_than=None,
                 at_specific_value=None,
                 first_val=0):
        self.at_relative = at_relative if (isinstance(at_relative, float) or at_relative is None) \
            else 1. / float(at_relative)
        self.if_first_iteration = if_first_count
        self.if_last_count = if_last_count
        self.first_val = first_val
        super().__init__(name=name, observable=observable, divisible_by=at_every, if_less_than=if_less_than,
                         if_more_than=if_more_than, at_specific_value=at_specific_value)

    def _update_status(self, *, new_val, method, other, previous):
        # Standard integer conditions
        super()._update_status(new_val=new_val, method=method, other=other, previous=previous)

        # First iteration
        if self.if_first_iteration and new_val == self.first_val:
            self._reason = f"First count."
            self._status = True
            return

        # Last iteration
        if self.if_last_count:
            last_count = self._observable.final_value
            if new_val == last_count:
                self._reason = f"Last count."
                self._status = True
                return

        # Relative
        if self.at_relative is not None:
            last_count = self._observable.final_value
            step = round(last_count * self.at_relative)
            if (new_val % step) == 0:
                self._reason = f"Iteration divisible by {step} " \
                               + f"(increase by {self.at_relative:%} of total iterations)"
                return True


if __name__ == "__main__":
    from observable_primitives import ObservableInteger

    obs_int = ObservableInteger(-2, 10)
    int_condition = CounterConditionObserver(observable=obs_int,
                                             at_every=[3, 7],
                                             if_less_than=-1,
                                             if_more_than=9,
                                             at_specific_value=[2, 6],
                                             if_first_count=True,
                                             if_last_count=True,
                                             at_relative=.5)

    # print(f"Counter {obs_int:3d}, condition {bool(int_condition)!r:5s}, reason {int_condition._reason}")
    for i in obs_int.range(-2, 12):
        print(f"Counter {obs_int:3d}, condition {bool(int_condition)!r:5s}, reason {int_condition._reason}")
