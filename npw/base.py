import npw
from npw.exceptions import NpwTypeError, NpwException
from npw.utils.logger import logger


class BaseObject(object):
    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self, data=None):
        return '<npw:{} | {}>'.format(self.__class__.__name__, data)


class BaseWrapperObject(object):
    def __init__(self, navisworks_object):
        self._wrapped = navisworks_object

    def __repr__(self, data=None):
        return '<npw:{} % {} {}>'.format(self.__class__.__name__,
                                         self._wrapped.ToString(),
                                         data)

    def unwrap(self):
        return self._wrapped
