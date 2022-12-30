
# php5random.py

php5random.py is a library which provides CPython bindings of the PHP 5 implementation of the random number generator, written in Rust!

## Usage

```python
from php5random import Php5Random

seed = 1337

rng = Php5Random(seed)
print(rng.rand_range(1, 100))  # prints 14
print(rng.rand())  # prints 1638893262
```

## Why?

I needed an implementation of the `rand` and `srand` functionality you'd find in `libc`, but:

- the values aren't consistent cross-platform
- it's not thread-safe

...and this solves that *blazingly fast!*

---

*PRs welcome!*
