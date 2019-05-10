# -*- coding: utf-8 -*-

# from keenepyt.pyt.toolfactory import ToolFactory
from keenepyt.pyt.tool import Tool
from keenepyt.pyt.tool2 import Tool2
# from keenepyt.pyt.tool5 import Tool5

# TOOL_FACTORY = ToolFactory()
# TOOL_FACTORY.import_tools()

from keenepyt.pyt.toolbin import *
# from keenepyt.pyt.tool5 import *

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "asdf"

        # List of tool classes associated with this toolbox
        # factory = ToolFactory()
        # factory.import_tools()
        # self.tools = factory.get_tools()
        self.tools = get_tools()
        # self.tools.append(Tool2)
        # self.tools.append(Tool3)
        # for tool in self.tools:
        #     import tool
        # tool = self.tools[1]()
        # self.tools.append(tool)
        with open(r'c:\temp\tools.txt', 'w') as f:
            f.write(str(self.tools))
        # self.tools = [Tool]

class Tool3(Tool):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool3"
        self.description = ""
        self.canRunInBackground = False
