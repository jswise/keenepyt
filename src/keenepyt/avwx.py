"""Define the AvWx class."""

import arcpy
import arcgis
import io
import pandas as pd
import pathlib
import requests

from keenepyt.core.thing import Thing

class AvWx(Thing):
    """Wraps the aviation weather service."""

    def get_aireps(self, mock=False):
        """Get aircraft weather reports.

        :param mock: Get reports from a file instead of online

        :return: A spatial dataframe containing aircraft weather reports
        """

        # Get the data as text (CSV with extra lines at the top).
        aireps_text = self.get_aireps_text(mock)

        # Convert the text to a Pandas dataframe.
        string_io = pd.compat.StringIO(aireps_text)
        df = pd.read_csv(string_io, header=5, index_col=False)

        # Convert the dataframe to an ArcGIS spatial dataframe.
        return arcgis.features.SpatialDataFrame.from_xy(
            df,
            'longitude',
            'latitude'
        )

    def get_aireps_text(self, mock=False):
        """Get aircraft weather reports as text (CSV with extra lines at the top).

        :param mock: Get reports from a file instead of online

        :return: A string containing weather data
        """

        # If we're mocking, get data from a file.
        if mock:
            repo_dir = pathlib.PurePath(__file__).parent.parent.parent
            file_path = pathlib.PurePath(repo_dir, 'data', 'aircraftreports.csv')
            with open(file_path) as f:
                return f.read()

        # If we want real data, call the National Weather Service.
        url = 'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=aircraftreports&requestType=retrieve&format=csv&hoursBeforeNow=0.5'
        try:
            response = requests.post(url)
        except Exception as e:
            message = 'HTTP request failed. ' + str(e)
            raise RuntimeError(message)
        if response.status_code != 200:
            message = 'HTTP request status {}. {}'.format(response.status_code, response.reason)
            raise RuntimeError(message)
        return response.text

    def write_aireps_fc(self, gdb, fc_name, mock=False):
        """Get aircraft weather reports, and write them to a feature class.

        :param gdb: The path to a geodatabase
        :param fc_name: The name of a future or existing feature class
        :param mock: Get reports from a file instead of online

        :return: The path to the feature class
        """

        if not arcpy.Exists(gdb):
            raise RuntimeError('The geodatabase does not exist ({}).'.format(gdb))
    
        sdf = self.get_aireps(mock)
        fc = pathlib.PurePath(gdb, fc_name)
        if arcpy.Exists(fc):
            self.info('Deleting {}.'.format(fc))
        self.info('Writing {}.'.format(fc))
        return sdf.to_featureclass(gdb, fc_name)
