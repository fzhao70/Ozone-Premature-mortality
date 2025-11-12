"""
Ozone Premature Mortality Calculator

A Python package for calculating premature mortality attributable to ozone exposure.
"""

from .mortality_calculator import mort_R, mort_C, mort_L

__version__ = "1.0.0"
__author__ = "fzhao70"

__all__ = ["mort_R", "mort_C", "mort_L"]
