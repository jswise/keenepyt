import logging
import pytest

from keenepyt.tools.hello import Hello

@pytest.fixture
def victim():
    return Hello(log_level=logging.INFO)

def test_execute(victim):
    victim.execute([], None)

if __name__ == '__main__':
    pytest.main([__file__])