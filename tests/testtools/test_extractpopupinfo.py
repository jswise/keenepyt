import logging
import os
import pathlib
import pytest

import arcpy

from keenepyt.core.kpworkspace import KPWorkspace
from keenepyt.tools.extractpopupinfo import ExtractPopupInfo

def get_fc():
    """Find or create the feature class to use for testing."""

    # Build the paths to the data.
    ws = KPWorkspace()
    ws_folder = ws.get_path()
    gdb = os.path.join(ws_folder, 'Peaks.gdb')
    fc = os.path.join(gdb, 'Placemarks', 'Points')
    backup_fc = fc + '_Backup'

    # If the file geodatabase exists, then delete the feature class,
    # and make a fresh copy from the backup.
    if arcpy.Exists(gdb):
        arcpy.management.Delete(fc)
        arcpy.management.CopyFeatures(backup_fc, fc)
    
    # If it doesn't exist, then create it by converting the KMZ.
    else:
        ws.info('File geodatabase not found. Converting KMZ to FGDB.')
        repo_dir = pathlib.PurePath(__file__).parent.parent.parent
        kmz = str(pathlib.PurePath(repo_dir, 'data', 'Peaks.kmz'))
        arcpy.conversion.KMLToLayer(kmz, ws_folder)
        arcpy.management.CopyFeatures(fc, backup_fc)

    return fc

@pytest.fixture
def victim():
    return ExtractPopupInfo(log_level=logging.INFO)

def test_execute(victim):
    fc = get_fc()
    fl = arcpy.management.MakeFeatureLayer(fc, 'fl')
    params = victim.getParameterInfo()
    params[0].value = fl
    victim.execute(params, None)

if __name__ == '__main__':
    pytest.main([__file__])