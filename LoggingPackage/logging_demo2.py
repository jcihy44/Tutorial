import logging
import LoggingPackage.custom_logger as cl

class LoggingDemo2():

    log = cl.customLogger(logging.DEBUG)

    # using the m-Log lines will make it so that all of the methods show logs in different files
    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method2(self):
        # if you wanted all the logs to be in the same file, then remove the m2Log lines
        # m2Log = cl.customLogger(logging.INFO)
        # m2Log.debug('debug message')
        # m2Log.info('info message')
        # m2Log.warning('warn message')
        # m2Log.error('error message')
        # m2Log.critical('critical message')

        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    def method3(self):
        # if you wanted all the logs to be in the same file, then remove the m3Log lines, same as above
        # m3Log = cl.customLogger(logging.INFO)
        # m3Log.debug('debug message')
        # m3Log.info('info message')
        # m3Log.warning('warn message')
        # m3Log.error('error message')
        # m3Log.critical('critical message')

        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()