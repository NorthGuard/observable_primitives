# observable_primitives
Implements emulations of python primitives, which are observable (notifies observers) when using augmented 
arithmetic (ex. +=, -=, etc.).

For example `ObservableInteger` can be used exactly as a normal integer. All arithmetics are performed as expected of 
an integer (`+`, `-`, `divmod()`, `//`, `str()`, `repr()` etc.). If any of the augmented arithmetics are called, 
updating the value of the integer, then all observers are notified (`+=`, `-=`, `*=`, `//=` etc.).

The available observables are:
* `ObservableInteger`
* `ObservableBool`
* `ObservableFloat`
* `ObservableComplex`


### Basic usage

```Python
from observable_primitives import ObservableInteger, NumericPrintObserver

# Make an observable primitive (initialized at 10)
obs_int = ObservableInteger(val=10)

# Make observer (simply prints notified changes)
observer = NumericPrintObserver(obs_int)

# Operations which observer is not notified of
print(obs_int)
print(2 + obs_int)
print(obs_int * 3)
print(obs_int // 3)
print(obs_int / 3)
print(obs_int % 3)
# 10
# 12
# 30
# 3
# 3.3333333333333335
# 1

# Change value of observable. This notifies observer which prints notification.
obs_int += 3
obs_int *= 5
# NumericPrintObserver(10 __iadd__ 3 = 13)
# NumericPrintObserver(13 __imul__ 5 = 65)

print(obs_int)
# 65
```


### Implementing Observers

Custom-made observers can be made by subclassing `Observer` and implementing the `observe`-method with signature:
```
observe(self, *args, **kwargs)
```

For `ObservableInteger`, `ObservableBool`, `ObservableFloat` and `ObservableComplex`, the arguments passed 
on to `observe` are:
```Python
args = []
kwargs = {
    'previous': PPP,
    'method': MMM,
    'other': OOO,
    'new_val': NNN
}
```
Where `PPP` is the value the observable had before the operation, `MMM` is the name of the invoked operation 
(ex. `__iadd__`), `OOO` is the other value use in the operation (ex. adding 4 to an integer) and `NNN` is
the value of the observable after the operation. 