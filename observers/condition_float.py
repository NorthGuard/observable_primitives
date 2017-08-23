from observable_primitives.observers.condition_observer_base import ConditionObserver


class FloatConditionObserver(ConditionObserver):
    def __init__(self, name=None, observable=None, if_less_than=None, if_more_than=None,
                 if_extreme_decrease_absolute=None,
                 if_extreme_decrease_relative=None,
                 if_extreme_increase_absolute=None,
                 if_extreme_increase_relative=None):
        super().__init__(name=name, observables=observable)
        self._if_less_than = float(if_less_than)
        self._if_more_than = float(if_more_than)
        self._if_extreme_decrease_absolute = float(if_extreme_decrease_absolute)
        self._if_extreme_decrease_relative = float(if_extreme_decrease_relative)
        self._if_extreme_increase_absolute = float(if_extreme_increase_absolute)
        self._if_extreme_increase_relative = float(if_extreme_increase_relative)

        self._observable = observable
        self._max_extreme = None
        self._min_extreme = None

        # Initialize
        self._initialize()

    def _initialize(self):
        self._update_status(new_val=self._observable.val, method="ObserverInitialize", other=None, previous=None)

    def _update_status(self, *, new_val, method, other, previous):
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

        # Note if value has been observed
        if self._max_extreme is None:
            self._max_extreme = self._min_extreme = new_val

        # Note for extreme changes
        else:

            # Check for absolute increase
            if self._if_extreme_increase_absolute is not None:
                if new_val - self._max_extreme >= self._if_extreme_increase_absolute:
                    self._reason = f"Value increased by more than {self._if_extreme_increase_absolute}" \
                                   f" ({self._max_extreme} -> {new_val})"
                    self._status = True
                    self._max_extreme = new_val
                    return

            # Check for absolute decrease
            if self._if_extreme_decrease_absolute is not None:
                if self._min_extreme - new_val >= self._if_extreme_decrease_absolute:
                    self._reason = f"Value decreased by more than {self._if_extreme_decrease_absolute}" \
                                   f" ({self._min_extreme} -> {new_val})"
                    self._status = True
                    self._min_extreme = new_val
                    return

            # Check for relative increase
            if self._if_extreme_increase_relative is not None:
                try:
                    diff = (new_val - self._max_extreme) / abs(self._max_extreme)
                    if diff >= self._if_extreme_increase_relative:
                        self._reason = f"Value increased by more than {self._if_extreme_increase_relative:.2%}" \
                                       f" ({self._max_extreme} -> {new_val})"
                        self._status = True
                        self._max_extreme = new_val
                        return
                except ZeroDivisionError:
                    pass

            # Check for relative decrease
            if self._if_extreme_decrease_relative is not None:
                try:
                    diff = (self._min_extreme - new_val) / abs(self._min_extreme)
                    if diff >= self._if_extreme_decrease_relative:
                        self._reason = f"Value decreased by more than {self._if_extreme_decrease_relative:.2%}" \
                                       f" ({self._min_extreme} -> {new_val})"
                        self._status = True
                        self._min_extreme = new_val
                        return
                except ZeroDivisionError:
                    pass

        # Don't select iteration
        self._reason = None
        self._status = False


if __name__ == "__main__":
    from observable_primitives import ObservableFloat

    obs_float = ObservableFloat(0)

    float_condition = FloatConditionObserver(
        name="FloatCondition",
        observable=obs_float,
        if_less_than=-3,
        if_more_than=4.5,
        if_extreme_increase_absolute=3,
        if_extreme_increase_relative=0.30,
        if_extreme_decrease_absolute=2,
        if_extreme_decrease_relative=0.50,
    )

    def evaluate():
        print(f"Counter {obs_float: 6.2f}, condition {bool(float_condition)!r:5s}, reason {float_condition._reason}")


    evaluate()
    obs_float -= 2
    evaluate()
    obs_float -= 1
    evaluate()
    obs_float -= 1
    evaluate()
    obs_float += 4
    evaluate()
    obs_float += 3
    evaluate()
    obs_float += 1
    evaluate()
    obs_float += 1
    evaluate()
    obs_float -= 5
    evaluate()
