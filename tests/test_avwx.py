import logging
import pytest

from keenepyt.avwx import AvWx

@pytest.fixture
def victim():
    return AvWx(log_level=logging.INFO)

def test_init(victim):
    pass

if __name__ == '__main__':
    pytest.main([__file__])