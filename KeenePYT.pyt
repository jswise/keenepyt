from keenepyt.tools.toolfactory import * # pylint: disable=unused-wildcard-import

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = 'KeenePYT Tools'
        self.alias = 'KeenePYT'
        self.description = 'Demonstration code from a workshop at Spring NEARC 2019.'

        self.tools = get_tools()
