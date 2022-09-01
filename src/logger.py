"""logger module for the project"""

import logging

class Logger():
    """Class to handle the logger of the project"""
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.log_console_format = "%(asctime)s [%(levelname)s]: %(message)s"
        self.set_console_handler()

    def set_console_handler(self):
        """function to set the console as the output of the program"""
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(self.log_console_format))
        self.logger.addHandler(console_handler)

    def set_log_level(self, level):
        """function to set the log level of the program"""
        self.logger.setLevel(level)
