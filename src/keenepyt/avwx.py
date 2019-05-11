"""Define the AvWx class."""

import pandas as pd
import requests

from keenepyt.core.thing import Thing

class AvWx(Thing):
    """Wraps the aviation weather service."""

    def get_aireps(self):
        url = 'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=aircraftreports&requestType=retrieve&format=csv&hoursBeforeNow=1'