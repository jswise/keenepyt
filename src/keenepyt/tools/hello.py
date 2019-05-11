"""Define the Hello class."""

from keenepyt.core.pyttool import PYTTool

class Hello(PYTTool):
    """Says hello."""

    def execute(self, parameters, messages):
        """Say hello."""

        self.info('Hello, NEARC!')
