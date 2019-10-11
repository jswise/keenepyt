"""Define the ExtractPopupInfo class."""

import arcpy

from keenepyt.core.pyttool import PYTTool
from keenepyt.exkml import ExKML

class ExtractPopupInfo(PYTTool):
    """Extracts popup info from a feature class that used to be part of a KML file."""

    def init_parameter_info(self):
        """Set the parameters for the tool."""

        self.add_param(
            'fl',
            'Feature Layer (former KML/KMZ)',
            datatype='GPFeatureLayer'
        )

    def execute(self, parameters, messages):
        """Extract the data."""

        params = self.get_param_val_dict(parameters)
        fl = params['fl']
        fc = fl.dataSource
        ek = ExKML(fc)
        ek.extract_popup_info()