import logging
import pytest

from keenepyt.core.thing import Thing

@pytest.fixture
def victim():
    return Thing(log_level=logging.DEBUG)

def test_init(victim):
    victim.debug('Thing initialized.')

def test_raise_error(victim):
    with pytest.raises(Exception):
        victim.raise_error('Bogus error')

if __name__ == '__main__':
    pytest.main([__file__])