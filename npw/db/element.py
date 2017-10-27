"""Wrapper for Navisworks.Api.ModelItem."""

from npw import base
from npw.db.propertygroup import PropertyCategory


class Element(base.BaseWrapperObject):
    def __init__(self, nw_modelitem):
        base.BaseWrapperObject.__init__(self, nw_modelitem)

    @property
    def property_categories(self):
        return self._wrapped.PropertyCategories

    def _lookup_propcat(self, param_name):
        for pc in self.property_categories:
            if pc.DisplayName == param_name \
                    or pc.Name == param_name:
                return pc

    def __getitem__(self, param_name):
        pcat = self._lookup_propcat(param_name)
        if pcat:
            return PropertyCategory(pcat)

        raise AttributeError('Property category does not exist: {}'
                             .format(param_name))

    def __contains__(self, key):
            return key in [x.DisplayName for x in self.property_categories]
