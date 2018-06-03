"""
Copyright (c) 2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""


class PiHoleError(Exception):
    """General PiHoleError exception occurred."""

    pass


class PiHoleConnectionError(PiHoleError):
    """When a connection error is encountered."""

    pass
