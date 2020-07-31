# __init__.py
__version__ = "0.0.8"
__author__ = "Fabien Nugier"

"""
The :mod:`scifin.timeseries` module includes methods for time series analysis.
"""

from .timeseries import timeseries, multi_plot
from .randomseries import auto_regressive, random_walk, drift_random_walk, moving_average, \
                          ARMA, RCA, ARCH, GARCH, CHARMA

