"""Define the PYTTool class."""

import arcpy

from keenepyt.core.thing import Thing

class PYTTool(Thing):
    """Provide the framework for ArcGIS Python toolbox (PYT) tools."""

    alias = None
    canRunInBackground = None
    category = None
    description = None
    label = None
    parameter_info = None
    tools = None

    def __init__(self, helpers=None, **args):
        """Initialize basic tool properties."""

        super().__init__(helpers, **args)
        self.description = 'Terracon tool'
        self.canRunInBackground = True
        self.alias = self.__class__.__name__
        self.set_tags()
        self.parameter_info = []
        self.init_parameter_info()

    def add_param(self, name, displayName=None, **kwargs):
        direction = kwargs.get('direction', 'Input')
        datatype = kwargs.get('datatype')
        parameterType = kwargs.get('parameterType', 'Required')
        enabled = kwargs.get('enabled')
        category = kwargs.get('category')
        symbology = kwargs.get('symbology')
        multiValue = kwargs.get('multiValue')
        defaultValue = kwargs.get('defaultValue')
        value_list = kwargs.get('valueList')

        if displayName is None:
            displayName = name.replace('_', ' ')
        if datatype is None:
            if isinstance(defaultValue, bool):
                datatype = 'GPBoolean'
            else:
                datatype = 'GPString'

        new_param = arcpy.Parameter(
            name,
            displayName,
            direction,
            datatype,
            parameterType,
            enabled,
            category,
            symbology,
            multiValue
        )

        new_param.value = defaultValue

        if value_list:
            new_param.filter.type = 'ValueList'
            new_param.filter.list = value_list

        self.parameter_info.append(new_param)
        return new_param

    def execute(self, parameters, messages):
        """Run the tool."""

        return
        
    def get_param_dict(self, parameters):
        """Put the tool parameter objects in a dictionary so they're easier to find."""

        param_dict = {}
        for param in parameters:
            if param.datatype == 'Boolean' and param.value is None:
                param.value = False
            param_dict[param.name] = param
        return param_dict

    def getParameterInfo(self):
        """Provide parameter definitions."""

        return self.parameter_info

    def get_param_val_dict(self, parameters):
        """Put the tool input values in a dictionary so they're easier to find."""

        param_dict = self.get_param_dict(parameters)
        for key, param in param_dict.items():
            if param.datatype == 'GPFeatureRecordSetLayer':
                param_dict[key] = param
            else:
                try:
                    val = param.value.value
                except AttributeError:
                    val = param.value
                param_dict[key] = val
        return param_dict

    def init_parameter_info(self):
        """Set the parameters for the tool."""

        pass

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def set_tags(self):
        """Set the name that people see."""

        self.label = self.alias

    def set_tool_param_value(self, parameters, paramname, value):
        for parameter in parameters:
            if parameter.name == paramname:
                parameter.value = value
                return
        self.error('Tool parameter "%s" "not found.' % paramname)
        raise RuntimeError

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return
