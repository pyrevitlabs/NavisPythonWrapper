"""Wrappers for Navisworks API classes."""

from npw.db import element


def wrap(nvswrks_mi):
    return element.Element(nvswrks_mi)
