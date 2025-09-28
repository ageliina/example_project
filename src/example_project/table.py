#!/usr/bin/env python3
# encoding: utf-8
# Author: Akke Viitanen
# Email: akke.viitanen@helsinki.fi
# Date: 2025-09-28 15:26:26

"""Handle tables."""

from astropy.table import Table
import astropy.units as u


def write_test_latex_table() -> None:
    """Write a test LaTeX table."""
    table = Table.read("data/tests/test_table.txt", format="ascii")
    table["a"] *= u.m
    table["b"] *= u.s
    table["c"] *= u.m / u.s
    table.write(
        "data/tests/test_table.tex",
        format="latex",
        latexdict=dict(
            tabletype="table*",
            tablealign="htbp",
            col_align="rrr",
            caption="Example table with units.",
            preamble="% preamble",
            header_start=r"\hline\hline",
            header_end=r"\hline",
            data_start="% data_start",
            data_end="% data_end",
            tablefoot=r"\tablefoot{This is a table footer for extra information.}",
        ),
        overwrite=True,
    )
