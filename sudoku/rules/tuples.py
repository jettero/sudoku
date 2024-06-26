#!/usr/bin/env python
# coding: utf-8
"""
CASE 0:
    If 5 and 8 appear in only in r2 and r3 of c1, then they can't also contain
    other numbers — remove anything but 5 and 8 from those two. This works for
    any N numbers in any N elements in any row/col/box.

CASE 1:
    If we do find a pair or triple or whatever, then remove those values from
    the other cells in the row/col/box as well.
"""

from itertools import combinations
from sudoku.rules import hookimpl
from sudoku.const import SEV
from sudoku.tools import describe_elements, format_ints

TUPLE_SIZEZ_AND_NAMES = (  # (sz, name), ...
    (1, "can only be"),
    (2, "pair"),
    (3, "triple"),
    (4, "quad"),
)


@hookimpl
def main(puzzle, opts=set()):
    did_count = 0

    for N, nname in TUPLE_SIZEZ_AND_NAMES:
        # CASE 0:
        for container in puzzle.containers:
            for vp in combinations(SEV - {e.value for e in container if e.value}, N):
                vp = {*vp}
                ep = {x for x in container if x.center & vp}

                if len(ep) == N:
                    removed = set()
                    if N == 1:
                        item, = ep
                        v, = vp
                        if item.value != v:
                            did_count += 1
                            item.value = v
                            puzzle.rows[item.row].remove_marks(v)
                            puzzle.cols[item.col].remove_marks(v)
                            puzzle.boxes[item.box].remove_marks(v)
                            removed.add(item)
                    else:
                        for item in ep:
                            if ov := item.center - vp:
                                item.remove_center_marks(*ov)
                                removed.add(item)
                                did_count += 1
                    if removed:
                        puzzle.describe_inference(
                            f"{format_ints(*vp)} {nname} in {describe_elements(ep)} in {container.short}"
                            f" -- remove other values from {describe_elements(removed)}",
                            __name__,
                        )

        # CASE 1:
        for container in puzzle.containers:
            nv = {x for x in container if not x.value}
            for ep in combinations(nv, N):
                ep = {*ep}
                vp = {x for y in ep for x in y.center}
                if len(vp) == N:
                    removed = set()
                    for item in nv - ep:
                        if item.center & vp:
                            item.remove_center_marks(*vp)
                            removed.add(item)
                            did_count += 1
                    if removed:
                        puzzle.describe_inference(
                            f"{format_ints(*vp)} {nname} in {describe_elements(ep)} in {container.short}"
                            f" -- remove values from {describe_elements(removed)}",
                            __name__,
                        )

    return did_count
