import logging
import os
import pathlib
import pytest

print('Importing ArcPy.')
import arcpy
from arcpy.da import SearchCursor # pylint: disable=no-name-in-module
print('Imported.')

from keenepyt.core.kpworkspace import KPWorkspace
from keenepyt.exkml import ExKML

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
        repo_dir = pathlib.PurePath(__file__).parent.parent
        kmz = str(pathlib.PurePath(repo_dir, 'data', 'Peaks.kmz'))
        arcpy.conversion.KMLToLayer(kmz, ws_folder)
        arcpy.management.CopyFeatures(fc, backup_fc)

    return fc

def get_victim():
    fc = get_fc()
    return ExKML(fc, log_level=logging.INFO)

def test_field_exists():
    victim = get_victim()
    assert victim.field_exists('PopupInfo')
    assert not victim.field_exists('Bogus')

def test_extract_popup_info():
    victim = get_victim()
    victim.extract_popup_info()

def test_get_popup_dict():
    victim = get_victim()
    cursor = SearchCursor(victim.fc, 'PopupInfo')
    row = cursor.next()
    html = row[0]
    del row
    del cursor
    popup_dict = victim.get_popup_dict(html)
    assert 'Elevation' in popup_dict

if __name__ == '__main__':
    pytest.main([__file__])
