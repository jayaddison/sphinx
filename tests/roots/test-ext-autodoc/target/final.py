from __future__ import annotations

import typing
from typing import final
from typing import final as final_ext

import typing_extensions


@typing.final
class Class:
    """docstring"""

    @final
    def meth1(self):
        """docstring"""

    def meth2(self):
        """docstring"""

    @final_ext
    def meth3(self):
        """docstring"""

    @typing_extensions.final
    def meth4(self):
        """docstring"""
