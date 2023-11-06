"""Test the add function in my_module.py."""

from pymatgen.analysis.myaddon.my_module import add


def test_add():
    """Pytest auto-discovers test_ prefixed functions in files with a test_ prefix."""
    expected = 2
    assert add(1, 1) == expected
