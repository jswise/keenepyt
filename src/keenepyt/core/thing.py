"""Define the Thing class, which all classes except reporters inherit."""

import os
import sys

from keenepyt.core.reporter import Reporter

class Thing:
    """Provide basic functionality for all KeenePYT classes."""

    helpers = None
    reporter = None

    def __init__(self, helpers=None, **args):
        self.init_helpers(helpers, **args)

    def critical(self, msg):
        """Show & log a really important error message."""

        self.reporter.critical(msg)

    def debug(self, msg):
        """Show & log a message that's only important when debugging."""

        self.reporter.debug(msg)

    def error(self, msg):
        """Show & log an error message."""

        self.reporter.error(msg)

    def info(self, msg):
        """Show & log an ordinary message."""

        self.reporter.info(msg)

    def init_helpers(self, helpers=None, **args):
        """Instantiate an object whose attributes will be helpful objects.

        The main purpose of the object is to hold the reporter,
        which ReporterUser will add.

        Override this method to instantiate other helpful objects and add
        them to self.helpers."""

        self.helpers = helpers

        if self.helpers is None:

            # Define a class that doesn't do anything except hold stuff.
            class Holder:
                """A class to hold helper objects.

                This seems to work better than a dictionary for
                passing references around."""
                pass

            # Instantiate the helpers object, which every other object
            # (except the reporter) will share.
            self.helpers = Holder()

        try:
            self.reporter = self.helpers.reporter
        except AttributeError:
            self.init_reporter(**args)

    def init_reporter(self, **args):
        """Initialize the reporter that all objects will use."""

        execname = os.path.basename(sys.executable)
        if execname.lower() == 'python.exe':
            self.reporter = Reporter(**args)
        else:
            from keenepyt.core.reporterarc import ReporterArc
            self.reporter = ReporterArc(**args)
        self.helpers.reporter = self.reporter

    def warning(self, msg):
        """Show & log a warning message."""

        self.reporter.warning(msg)
