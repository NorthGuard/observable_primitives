from observable_primitives import ObservableInteger
from observable_primitives import IntegerConditionObserver
from observable_primitives.observers.condition_observer_base import MultiConditionObserver


if __name__ == "__main__":

    obs_int1 = ObservableInteger(0)
    obs_int2 = ObservableInteger(0)
    obs_int3 = ObservableInteger(0)
    cond1 = IntegerConditionObserver(name="IntCond1", observable=obs_int1, if_more_than=0)
    cond2 = IntegerConditionObserver(name="IntCond2", observable=obs_int2, if_more_than=0)
    cond3 = IntegerConditionObserver(name="IntCond3", observable=obs_int3, if_more_than=0)

    multi_observe = (cond1 | (cond2 & cond3)) + "Combination"  # type: MultiConditionObserver

    def evaluate():
        str1 = f"Integers {obs_int1}, {obs_int2}, {obs_int3}: "
        # str2 = f"multi-observer {bool(multi_observe)!r:5s}, reason {multi_observe._reason}"
        print(str1 + multi_observe.report())

    evaluate()
    obs_int1 += 1
    evaluate()
    obs_int1 -= 1
    evaluate()
    obs_int2 += 1
    evaluate()
    obs_int3 += 1
    evaluate()
