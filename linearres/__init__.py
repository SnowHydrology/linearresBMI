"""Simulate discharge with a linear reservoir model."""
from ._version import __version__
from .bmi_linearres import LinearresBmi
from .linearres import Linearres, solve_linearres

__all__ = ["__version__", "LinearresBmi", "solve_linearres", "Linearres"]
