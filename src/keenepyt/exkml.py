"""Define the ExKML class."""

from keenepyt.core.thing import Thing

class ExKML(Thing):
    """Represents a feature class containing data that used to be in a KML file."""

    fc = None

    def __init__(self, fc, helpers=None, **kwargs):
        super().__init__(helpers, **kwargs)
        self.fc = fc
