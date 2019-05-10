from keenepyt.pyt.tool5 import Tool5
from keenepyt.pyt.tool2 import Tool2

class BinTool2(Tool2):
    pass

class BinTool5(Tool5):
    pass

def get_tools():
    return [BinTool2, BinTool5]