import logging

import pytest

from keenepyt.core.reporterarc import ReporterArc

"""
These tests pass even if ArcPy isn't available (i.e.
there's no ArcGIS license). I'm not sure why.
"""

@pytest.fixture
def victim():
    return ReporterArc()

def test_critical(victim):
    victim.critical('Fake critical message.')

def test_debug(victim):
    victim.debug('Fake debug message.')

def test_error(victim):
    victim.error('Fake error message.')

def test_get_caller(victim):
    caller = victim.get_caller()
    assert caller == 'ArcGIS'

def test_get_log_folder(victim):
    logfolder = victim.get_log_folder()
    assert 'KeenePYT' in logfolder

def test_info(victim):
    victim.info('Info message.')

def test_set_log_level(victim):
    victim.set_log_level(logging.DEBUG)
    victim.debug('You should see this.')
    victim.set_log_level(logging.INFO)
    victim.debug('You should not see this.')

def test_warning(victim):
    victim.warning('Fake warning message.')

if __name__ == '__main__':
    pytest.main([__file__])