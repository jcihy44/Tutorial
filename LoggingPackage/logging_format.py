"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

"""
Logging Format docs for playing around
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

import logging
# if you were to do %H instead of %I it makes it a 24 hour clock rather than the 12 hour clock
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")