""" Custom NPW exceptions."""  #


class NpwException(Exception):
    """Navis Python Wrapper Base Exception."""


class NpwTypeError(TypeError):
    """Navis Python Wrapper Base Exception."""

    def __init__(self, type_expected, type_received=None):
        type_received = type_received or 'not reported'
        msg = 'expected [{}], got [{}]'.format(type_expected, type_received)
        super(NpwTypeError, self).__init__(msg)


class NpwParameterNotFound(NpwException, KeyError):
    """Navis Python Wrapper Parameter Error."""

    def __init__(self, mi_guid, param_name):
        msg = 'parameter not found [element:{}]:[param_name:{}]'\
              .format(mi_guid, param_name)

        super(NpwParameterNotFound, self).__init__(msg)
