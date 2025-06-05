"""
Logger Demo

this code is utilizing the logging.conf as a reference logging file

altering the 'w' in the args line will change how the logs are written to the file, append, overwrite etc
[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('test1.log', 'w')

"""
import logging
import logging.config

class LoggerDemoConf():

    def testLog(self):
        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConf()
demo.testLog()