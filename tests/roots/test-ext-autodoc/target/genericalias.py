from __future__ import annotations

from typing import List
from collections.abc import Callable

#: A list of int
T = list[int]

C = Callable[[int], None]  # a generic alias not having a doccomment


class Class:
    #: A list of int
    T = list[int]


#: A list of Class
L = list[Class]
