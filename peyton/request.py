"""Module that contains classes for turning a request event into a python object."""


class RequestBase:
    """Base class for all Request classes."""

    pass


class Request(RequestBase):
    """Top level request class."""

    pass


class QueryStringParams(RequestBase):
    """Class for all query String Paramaters, both single and multi value."""

    pass


class PathParameters(RequestBase):
    """Class for all path parameters."""

    pass


class StageVariables(RequestBase):
    """Class for all Stage Variables."""

    pass


class Headers(RequestBase):
    """Load all headers into an object, both single and multi value."""

    pass


class RequestContext(RequestBase):
    """Load the request context into an object."""

    pass


class RequestIdentity(RequestBase):
    """Load the indentity of the request into an object."""

    pass
