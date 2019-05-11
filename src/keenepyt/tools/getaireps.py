"""Define the GetAireps class."""

import arcpy

from keenepyt.core.pyttool import PYTTool
from keenepyt.avwx import AvWx

class GetAireps(PYTTool):
    """Gets aircraft weather reports from the National Weather Service."""

    def init_parameter_info(self):
        """Set the parameters for the tool."""

        self.add_param(
            'gdb',
            'Workspace',
            datatype='DEWorkspace',
            defaultValue=arcpy.env.workspace # pylint: disable=no-member
        )
        self.add_param(
            'fc_name',
            'Feature Class Name',
            datatype='GPString',
            defaultValue='Aireps'
        )
        self.add_param(
            'fc',
            'Aireps Feature Class',
            datatype='DEFeatureClass',
            direction='Output',
            parameterType='Derived'
        )

    def execute(self, parameters, messages):
        """Get aireps."""

        params = self.get_param_val_dict(parameters)
        gdb = params['gdb']
        fc_name = params['fc_name']
        aviation_weather = AvWx(self.helpers)
        fc = aviation_weather.write_aireps_fc(gdb, fc_name)
        self.set_tool_param_value(parameters, 'fc', fc)