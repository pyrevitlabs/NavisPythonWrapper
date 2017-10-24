"""Wrapper for Navisworks.Api.ModelItem."""

from npw import base
from npw.db.property import Property


class Element(base.BaseObject):
    def __init__(self, nw_modelitem):
        self._wrapped_mi = nw_modelitem

    def __repr__(self, data=None):
        return base.BaseObject.__repr__(self, self._wrapped_mi.ToString())

    def _lookup_param(self, param_name):
        for pc in self._wrapped_mi.PropertyCategories:
            for dp in pc.Properties:
                if dp.DisplayName == param_name \
                        or dp.Name == param_name:
                    return dp

    def __getitem__(self, param_name):
        prop = self._lookup_param(param_name)
        if prop:
            return Property(prop)
