"""Linear reservoir model"""

import numpy as np
import yaml


def solve_linearres(precip, discharge, k, timestep_s):
    """Run the linearres model for one time step to update the states and fluxes.

    Parameters
    ----------
    precip : ndarray
        Precipitation (input from forcing data).
    discharge: ndarray
        Modeled discharge per time step (flux that gets updated).
    k: float
        Loss parameter for linear reservoir (parameter).
    timestep_s: float
        Model time step in seconds (parameter).

    Returns
    -------
    TODO

    Examples
    --------
    TODO
    """

    # Calculate timestep in days
    d_t = timestep_s/86400

    # Compute the new discharge using a linear reservoir function
    discharge_new = (discharge * np.exp(-k*d_t)) + (precip * (1 - np.exp(-k*d_t)))

    # Set discharge to the newly computed value
    np.add(0, discharge_new, out=discharge)

    return discharge


class Linearres(object):
    """Linear reservoir model class.

    Examples
    --------
    TODO

    """

    def __init__(
        self, k=0.5, discharge_init=0,
    ):
        """Create a new Linearres model.

        Parameters
        ---------

        """
        self._k = k

        self._time = 0.0
        self._time_step = 86400

        self._ppt_mm = np.zeros(1, dtype=float)
        self._q_mm = np.zeros(1, dtype=float)
        q_tmp = np.zeros(1, dtype=float)
        q_tmp[0, ] = discharge_init
        self._q_mm = q_tmp

    @property
    def k(self):
        """Linear reservoir loss parameter"""
        return self._k

    @property
    def time(self):
        """Current model time."""
        return self._time

    @property
    def time_step(self):
        """Model time step."""
        return self._time_step

    @property
    def ppt_mm(self):
        """Current precipitation."""
        return self._ppt_mm

    @ppt_mm.setter
    def ppt_mm(self, ppt_mm):
        """Set precipitation."""
        self._ppt_mm[:] = ppt_mm

    @property
    def q_mm(self):
        """Current discharge."""
        return self._q_mm

    @q_mm.setter
    def q_mm(self, q_mm):
        """Set discharge."""
        self._q_mm[:] = q_mm

    @classmethod
    def from_file_like(cls, file_like):
        """Create a Linearres object from a file-like object.

        Parameters
        ----------
        file_like : file_like
            Input parameter file.

        Returns
        -------
        Linearres
            A new instance of a Linearres object.
        """
        config = yaml.safe_load(file_like)
        return cls(**config)

    def advance_in_time(self):
        """Calculate discharge."""
        solve_linearres(
            self._ppt_mm,
            self._q_mm,
            self._k,
            self._time_step,
        )

        self._time += self._time_step
