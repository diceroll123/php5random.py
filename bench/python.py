import time
from ctypes import c_int, c_uint

# http://www.mscs.dal.ca/~selinger/random/


# just to prove the Rust version is faster, here's the Python version!
# it's mostly slower due to all the looping that goes into instantiation.


class Php5Random:
    def __init__(self, seed: int = 0) -> None:
        self._r = [0 for _ in range(34)]
        self._k = 0
        self._srand(seed)

    def _RAND_RANGE(
        self,
        __n: float,
        __min: float,
        __max: float,
    ) -> float:
        return __min + ((__max - __min + 1.0) * (__n / 2147483647))

    def _srand(self, seed: int = 0) -> None:
        self._r = [0 for _ in range(34)]
        self._r[0] = c_int(seed).value
        for i in range(1, 31):
            self._r[i] = (16807 * self._r[i - 1]) % 2147483647
        for i in range(31, 34):
            self._r[i] = self._r[i - 31]
        self._k = 0
        for _ in range(310):
            self.rand()

    def rand(self) -> int:
        self._r[self._k] = self._r[(self._k - 31) % 34] + self._r[(self._k - 3) % 34]
        r = c_uint(self._r[self._k]).value >> 1
        self._k = (self._k + 1) % 34
        return r

    def rand_range(self, min: int, max: int) -> int:
        return int(self._RAND_RANGE(self.rand(), min, max))


start_time = time.monotonic()
for _ in range(10000):
    rand = Php5Random(1)
    rand.rand_range(0, 100)
print("took", time.monotonic() - start_time, "seconds")
