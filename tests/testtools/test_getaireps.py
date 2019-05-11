import logging
import pytest

from keenepyt.tools.getaireps import GetAireps

GDB = r'c:\Projects\NEARC\Maps\KeenePYT\Default.gdb'

@pytest.fixture
def victim():
    return GetAireps(log_level=logging.INFO)

def test_execute(victim):
    params = victim.getParameterInfo()
    params[0].value = GDB
    victim.execute(params, None)

if __name__ == '__main__':
    pytest.main([__file__])