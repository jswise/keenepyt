import logging
import pytest

from keenepyt.tools.helloinput import HelloInput

@pytest.fixture
def victim():
    return HelloInput(log_level=logging.INFO)

def test_execute(victim):
    params = victim.getParameterInfo()
    params[0].value = 'Huck'
    victim.execute(params, None)

if __name__ == '__main__':
    pytest.main([__file__])