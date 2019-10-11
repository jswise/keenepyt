"""Define the Reporter class."""

import inspect
import logging
import logging.handlers
import os
import sys
import xml.etree.ElementTree as ET

class Reporter:
    """Default reporter for non-ArcPy environments."""

    log_level = None
    logger = None

    def __init__(self, log_level=logging.INFO, **kwargs):
        """Start logging."""

        self.start_logging(log_level)

    def critical(self, msg):
        """Show & log a really important error message."""

        self.logger.critical(msg)

    def debug(self, msg):
        """Show & log a message that's only important when debugging."""

        self.logger.debug(msg)

    def error(self, msg):
        """Show & log an error message."""

        self.logger.error(msg)

    def get_caller(self):
        """Find out what function started things."""

        prev_mod = None
        for frame in inspect.stack():

            # In Python 3.5 and above, the frame is a named tuple. In earlier
            # versions, it's just a list.
            try:
                file_name = frame.filename
            except:
                file_name = frame[1]
            if not 'keenepyt' in file_name:
                return prev_mod.__name__
            prev_mod = inspect.getmodule(frame[0])

    def get_log_folder(self):
        """Figure out where to put the log file.
        
        :return: The to a folder for log files
        """

        profile = os.environ['USERPROFILE']
        return os.path.join(
            profile,
            'AppData',
            'Local',
            'KeenePYT',
            'Logs'
        )
        
    def info(self, msg):
        """Show & log an ordinary message."""

        self.logger.info(msg)

    def set_log_level(self, log_level):
        """Set the logging level for the logger that we use for everything."""

        self.log_level = log_level
        self.logger.setLevel(log_level)

    def start_logging(self, log_level):
        """Set up logging & log a start message."""

        # Get a logger, and make sure we haven't already configured it.
        self.logger = logging.getLogger(__name__)
        if self.logger.handlers:
            return

        # Start with just stdout (print to screen).
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

        # Get the folder for log files.
        log_folder = self.get_log_folder()
        os.makedirs(log_folder, exist_ok=True)
        log_file_path = os.path.join(log_folder, 'KeeneLog')

        # Temporarily set the logging level, and print the
        # log folder path to the screen (there's no file yet).
        self.logger.setLevel(logging.INFO)
        self.info('Log folder:  %s' % log_folder)
        
        # Set up the log file handler.
        handler = logging.handlers.TimedRotatingFileHandler(log_file_path, 'midnight')
        formatter = logging.Formatter('%(asctime)s %(levelname)s:  %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Log the startup message.
        self.logger.info('______________________________________________________________')
        caller = self.get_caller()
        self.logger.info('Caller: %s' % caller)

        # Set the real logging level.
        self.set_log_level(log_level)

    def warning(self, msg):
        """Show & log a warning message."""

        self.logger.warning(msg)
