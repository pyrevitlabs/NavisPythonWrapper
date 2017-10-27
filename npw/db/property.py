"""Wrapper for Navisworks.Api.DataProperty."""

from npw import base
from npw import API


class Property(base.BaseObject):
    def __init__(self, nw_dataprop):
        self._wrapped = nw_dataprop

    @property
    def value(self):
        val = self._wrapped.Value
        if val.IsAnyDouble:
            return val.ToAnyDouble()
        elif val.IsBoolean:
            return val.ToBoolean()
        elif val.IsDateTime:
            return val.ToDateTime()
        elif val.IsDisplayString:
            return val.ToDisplayString()
        elif val.IsDouble:
            return val.ToDouble()
        elif val.IsDoubleAngle:
            return val.ToDoubleAngle()
        elif val.IsDoubleArea:
            return val.ToDoubleArea()
        elif val.IsDoubleLength:
            return val.ToDoubleLength()
        elif val.IsDoubleVolume:
            return val.ToDoubleVolume()
        elif val.IsIdentifierString:
            return val.ToIdentifierString()
        elif val.IsInt32:
            return val.ToInt32()
        elif val.IsNamedConstant:
            return val.ToNamedConstant()
        elif val.IsPoint2D:
            return val.ToPoint2D()
        elif val.IsPoint3D:
            return val.ToPoint3D()
        elif val.IsDisposed or val.IsNone:
            return None
