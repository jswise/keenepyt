"""Provide tools to the toolbox."""

from keenepyt.tools.getaireps import GetAireps
from keenepyt.tools.hello import Hello
from keenepyt.tools.helloinput import HelloInput

class GetAirepsLocal(GetAireps):
    def set_tags(self):
        """Set the name that people see."""

        self.category = 'Weather'
        self.label = 'Get Aircraft Weather Reports'

class HelloInputLocal(HelloInput):

    def set_tags(self):
        """Set the name that people see."""

        self.category = 'Test'
        self.label = 'Hello with Input'

class HelloLocal(Hello):

    def set_tags(self):
        """Set the name that people see."""

        self.category = 'Test'
        self.label = 'Hello'

def get_tools():
    return [
        # GetAirepsLocal,
        # HelloInputLocal,
        HelloLocal
    ]