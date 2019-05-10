# -*- coding: utf-8 -*-

from keenepyt.pyt.toolfactory import ToolFactory
from keenepyt.pyt.tool import Tool

TOOL_FACTORY = ToolFactory()

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "asdf"

        # List of tool classes associated with this toolbox
        factory = ToolFactory()
        self.tools = TOOL_FACTORY.get_tools()
        # self.tools = [Tool]