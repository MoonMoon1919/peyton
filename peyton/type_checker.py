"""Type checking module for Peyton."""


class DescriptorBase:
    """Descriptor base class that store values."""

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def typed(expected_type, cls=None):
    """Base Type checker decorator.

    Args:
        expected_type: A Type (str, dict, list, etc)
        cls: A python class, subclassed from DescriptorBase

    Returns:
        cls: returns class
    """
    if cls is None:
        return lambda cls: typed(expected_type, cls)

    super_set = cls.__set__

    def __set__(self, instance, val):
        """type checker.

        Args:
            instance: the name of the element (eg: "foo)
            val: the value of the element (eg: "bar")

        Raises:
            TypeError: in the event the type of the val is not the same as the expected type
        """
        if not isinstance(val, expected_type):
            raise TypeError("Expected " + str(expected_type))
        super_set(self, instance, val)

    cls.__set__ = __set__

    return cls


@typed(int)
class Integer(DescriptorBase):
    """Type checker for integers.

    Usage:
        Specify a type for an attribute with automatic type checking.

    Raises:
        TypeError: in the event the type of the object does not match specified type
    """

    pass


@typed(dict)
class Dictionary(DescriptorBase):
    """Type checker for Dictionaries.

    Usage:
        Specify a type for an attribute with automatic type checking.

    Raises:
        TypeError: in the event the type of the object does not match specified type
    """

    pass


@typed(str)
class String(DescriptorBase):
    """Type check for Strings.

    Usage:
        Specify a type for an attribute with automatic type checking.

    Raises:
        TypeError: in the event the type of the object does not match specified type
    """

    pass


@typed(list)
class List(DescriptorBase):
    """Type checker for Lists.

    Usage:
        Specify a type for an attribute with automatic type checking.

    Raises:
        TypeError: in the event the type of the object does not match specified type
    """

    pass


@typed(bool)
class Boolean(DescriptorBase):
    """Type checker for Boolean.

    Usage:
        Specify a type for an attribute with automatic type checking.

    Raises:
        TypeError: in the event the type of the object does not match specified type
    """

    pass
