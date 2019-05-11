import logging
import pytest

from keenepyt.core.pyttool import PYTTool

@pytest.fixture
def victim():
    return PYTTool(log_level=logging.DEBUG)

def test_execute(victim):
    victim.execute([], None)

if __name__ == '__main__':
    pytest.main([__file__])