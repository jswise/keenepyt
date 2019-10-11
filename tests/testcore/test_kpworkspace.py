import logging
import os
import pytest

from keenepyt.core.kpworkspace import KPWorkspace

@pytest.fixture
def victim():
    return KPWorkspace(log_level=logging.DEBUG)

def test_get_path(victim):
    ws_folder = victim.get_path()
    assert 'Workspace' in ws_folder
    assert os.path.exists(ws_folder)
