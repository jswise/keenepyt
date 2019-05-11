import logging
import pytest

from keenepyt.avwx import AvWx

GDB = r'c:\Projects\NEARC\Maps\KeenePYT\Default.gdb'

@pytest.fixture
def victim():
    return AvWx(log_level=logging.INFO)

def test_get_aireps(victim):
    victim.get_aireps(True)

def test_get_aireps_text(victim):
    text = victim.get_aireps_text(True)
    assert 'data source=aircraftreports' in text

def test_write_aireps_fc(victim):
    import arcpy
    fc = victim.write_aireps_fc(GDB, 'Aireps', True)
    assert arcpy.Exists(fc)

if __name__ == '__main__':
    pytest.main([__file__])