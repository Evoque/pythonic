
import typing
import collections.abc


count: int
counts: list[int] = []

# a dict with str keys, values are tuples containing 2 ints and a str
employee_data: dict[str, tuple[int, int, str]]
employee_data2: typing.Dict[str, typing.Tuple[int, int, str]]

# a callable taking a single str or bytes argument and returning a bool
str_predicate_function: typing.Callable[[str | bytes], bool]

# a dict with str keys, whose values are functions that take and return an int
str_function_map: dict[str, typing.Callable[[int], int]] = {
  'square': lambda x: x * x,
  'cube': lambda x: x * x * x
}

# Type Expression Parameters
ano_type: typing.Annotated[int, "this is hint", "this is hint 2"]

name: collections.abc.Sequence[str]