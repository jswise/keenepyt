"""Define the ReporterArc class."""

import logging

from keenepyt.core.reporter import Reporter

class ReporterArc(Reporter):
    """Reporter for ArcPy environments."""

    def __init__(self, log_level=logging.INFO):
        """Import ArcPy.
        
        On non-Esri machines, test discovery fails if a module tries to import ArcPy.
        That's why it's here and not on top.
        """

        super().__init__(log_level)
        try:
            import arcpy
        except ImportError:
            self.error('Failed to import ArcPy.')
            self.error('Make sure you have access to an ArcGIS license.')
            raise RuntimeError

    def critical(self, msg):
        """Show & log a really important error message."""
        
        # We've already imported ArcPy, but this line avoids throwing NameErrors.
        import arcpy

        super().critical(msg)
        arcpy.AddError(msg)

    def debug(self, msg):
        """Show & log a message that's only important when debugging."""
        
        # We've already imported ArcPy, but this line avoids throwing NameErrors.
        import arcpy

        super().debug(msg)
        if self.log_level == logging.DEBUG:
            arcpy.AddMessage(msg)

    def error(self, msg):
        """Show & log an error message."""
        
        # We've already imported ArcPy, but this line avoids throwing NameErrors.
        import arcpy

        super().error(msg)
        arcpy.AddError(msg)

    def get_caller(self):
        """Find out what function started things."""

        return 'ArcGIS'

    def info(self, msg):
        """Show & log an ordinary message."""
        
        # We've already imported ArcPy, but this line avoids throwing NameErrors.
        import arcpy

        super().info(msg)
        if self.log_level is None or self.log_level >= logging.INFO:
            arcpy.AddMessage(msg)

    def warning(self, msg):
        """Show & log a warning message."""
        
        # We've already imported ArcPy, but this line avoids throwing NameErrors.
        import arcpy

        super().warning(msg)
        arcpy.AddWarning(msg)
