"""Tests of custom exceptions."""
import pytest

from phonopy import Phonopy
from phonopy.exception import ForcesetsNotFoundError


def test_ForcesetsNotFoundError(ph_nacl_unitcell_order1: Phonopy):
    """Test of ForcesetsNotFoundError."""
    ph = ph_nacl_unitcell_order1
    with pytest.raises(ForcesetsNotFoundError):
        ph.produce_force_constants()
