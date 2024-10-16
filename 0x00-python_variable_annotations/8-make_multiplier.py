#!/usr/bin/env python3

"""
type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies the float
    """
    def multiplies(n: float):
        """
        multiplies two nums
        """
        return n * multiplier
    return multiplies
