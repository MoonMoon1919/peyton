"""Type checking module for Peyton."""


class DescriptorBase:
    """Descriptor base class that performs Type checking."""

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def typed(expected_type, cls=None):
    """Base Type checker class."""
    if cls is None:
        return lambda cls: typed(expected_type, cls)

    super_set = cls.__set__

    def __set__(self, instance, val):
        if not isinstance(val, expected_type):
            raise TypeError("Expected " + str(expected_type))
        super_set(self, instance, val)

    cls.__set__ = __set__

    return cls


@typed(int)
class Integer(DescriptorBase):
    """Type checker for integers."""

    pass


@typed(dict)
class Dictionary(DescriptorBase):
    """Type checker for Dictionaries."""

    pass


@typed(str)
class String(DescriptorBase):
    """Type check for Strings."""

    pass


@typed(list)
class List(DescriptorBase):
    """Type checker for Lists."""

    pass


@typed(bool)
class Boolean(DescriptorBase):
    """Type checker for Boolean."""

    pass
