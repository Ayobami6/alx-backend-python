#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Any, Union, Mapping, TypeVar

N = TypeVar('N')
Return = Union[Any, N]
Default = Union[Any, None]


def safely_get_value(dct: Mapping, key: Any, default: Default = None) -> Return:
    """Returns the value safely.

    Args:
        dct (Mapping): mapping
        key (Any): key
        default (Default, optional): default value. Defaults to None.

    Returns:
        Return: value
    """
    if key in dct:
        return dct[key]
    else:
        return default
