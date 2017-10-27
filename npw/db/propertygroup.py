"""Wrapper for Navisworks.Api.ModelItem."""

from npw import base
from npw.db.property import Property


class PropertyCategory(base.BaseObject):
    def __init__(self, nw_propgroup):
        self._wrapped = nw_propgroup

    def __repr__(self, data=None):
        return base.BaseObject.__repr__(self, self._wrapped.ToString())

    @property
    def properties(self):
        return self._wrapped.Properties

    def _lookup_prop(self, param_name):
        for dp in self.properties:
            if dp.DisplayName == param_name \
                    or dp.Name == param_name:
                return dp

    def __getitem__(self, param_name):
        dprop = self._lookup_prop(param_name)
        if dprop:
            return Property(dprop)

        raise AttributeError('Property does not exist: {}'
                             .format(param_name))

    def __contains__(self, key):
            return key in [x.DisplayName for x in self.properties]
