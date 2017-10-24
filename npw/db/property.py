"""Wrapper for Navisworks.Api.DataProperty."""

from npw import base
from npw import API


class Property(base.BaseObject):
    def __init__(self, nw_dataprop):
        self._wrapped_dp = nw_dataprop

    @property
    def value(self):
        val = self._wrapped_dp.Value
        if val.IsDisplayString:
            return val.ToDisplayString()
