"""Type checking module for Peyton."""


class DescriptorBase:
    """Descriptor base class that performs Type checking."""

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(DescriptorBase):
    """Base Type checker class."""

    expected_type = None

    def __set__(self, instance, val):
        if not isinstance(val, self.expected_type):
            raise TypeError("Expected " + str(self.expected_type))

        super().__set__(instance, val)


class Integer(Typed):
    """Type checker for integers."""

    expected_type = int


class Dictionary(Typed):
    """Type checker for Dictionaries."""

    expected_type = dict
