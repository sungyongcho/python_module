from collections.abc import Iterable


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
        Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
        Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    # ... Your code here ...
    if not isinstance(iterable, Iterable):
        raise TypeError("argument must support iteration")
    if not iterable:
        raise TypeError("argument empty")
    for elem in iterable:
        yield function_to_apply(elem)
