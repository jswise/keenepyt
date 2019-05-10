"""Define the ToolFactory class."""

from keenepyt.pyt.tool import Tool
# from keenepyt.pyt.tool2 import Tool2
from keenepyt.pyt.tool5 import Tool5

class ToolFactory:
    """Provides the toolbox with its list of tools."""

    def get_tools(self):
        """Provide a list of tools for a Python geoprocessing toolbox.

        :return: A list of tool classes.
        """

        return [Tool4, Tool5]
    
    def import_tools(self):
        from keenepyt.pyt.tool5 import Tool5

class Tool4(Tool):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool4"
        self.description = ""
        self.canRunInBackground = False
