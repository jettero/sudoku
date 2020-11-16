#!/usr/bin/env python
# coding: utf-8

import weakref
import sudoku.otuple as otuple
from .otuple import Otuple
from .element import Element
from .filt import (
    attrs_containing_val,
    val_restricted_to_single_attr,
    element_has_val,
    elements_in_attr,
)
from .const import BOX_NUMBERS


class Box:
    def __init__(self, *e, idx=None):
        if len(e) == 0:
            self._elements = Otuple(Element() for _ in range(9))
        elif len(e) == 9:
            self._elements = Otuple(weakref.ref(x) for x in e)
        else:
            raise ValueError(
                f"A {self.__class__} must receive 0 elements or 9, nothing in between"
            )

        if idx is not None:
            for e in self:
                e.tags.add(f"{self.ccode}{idx}")

    def has(self, val, inc_val=True, inc_marks=False):
        return set(
            x
            for x in self
            if element_has_val(x, val, inc_val=inc_val, inc_marks=inc_marks)
        )

    def attr_containing_val(self, val, attr="row", inc_val=True, inc_marks=True):
        return attrs_containing_val(
            self, val, attr=attr, inc_val=inc_val, inc_marks=inc_marks
        )

    def single_attr_containing_val(self, val, attr="row", inc_val=True, inc_marks=True):
        return val_restricted_to_single_attr(
            self, val, attr=attr, inc_val=inc_val, inc_marks=inc_marks
        )

    def elements_in_attr(self, no, attr="row"):
        return elements_in_attr(self, no, attr=attr)

    @property
    def cname(self):
        return self.__class__.__name__

    @property
    def lcname(self):
        return self.__class__.__name__.lower()

    @property
    def ccode(self):
        return self.__class__.__name__[0].lower()

    def __getitem__(self, i):
        e = self._elements[i]
        if isinstance(e, weakref.ref):
            return e()
        return e

    def __setitem__(self, i, v):
        self._elements[i].value = v

    def __iter__(self):
        yield from (self[i] for i in BOX_NUMBERS)

    def __repr__(self):
        e = " ".join(repr(e) for e in self)
        return f"{self.cname}[{e}]"

    @property
    def short(self):
        n = self.lcname
        return f"{n} {getattr(self[1], n)}"


class Row(Box):
    pass


class Col(Box):
    pass


otuple.BOX_CLASS = Box