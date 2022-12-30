
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

## Benchmarks

In the `bench` folder you'll find two files. `python.py`, and `rust.py`. After running them on my 8-core 2.4GHz Intel Mac from 2019, I get the following (rounded to 3 decimals):

- `python.py`: `1.221s`
- `rust.py`: `0.410s`

Making Rust nearly 3x faster!


---

*PRs welcome!*
