import time

from php5random import Php5Random

start_time = time.monotonic()
for _ in range(10000):
    rand = Php5Random(1)
    rand.rand_range(0, 100)
print("took", time.monotonic() - start_time, "seconds")
