from typing_extensions import Self

class Php5Random:

    def __new__(cls, seed: int) -> Self:
        """Constructs a new Php5Random object with the given seed."""
        ...

    def srand(self, seed: int) -> None:
        """Seeds the random number generator with the given seed."""
        ...

    def rand(self) -> int:
        """Returns a pseudo-random integer between 0 and 2147483647."""
        ...

    def rand_range(self, min: int, max: int) -> int:
        """Return a random integer N such that min <= N <= max."""
        ...

