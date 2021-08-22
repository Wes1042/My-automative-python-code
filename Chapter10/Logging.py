'''Python’s
logging module makes it easy to create a record of custom messages that
you write. These log messages will describe when the program execution has
reached the logging function call and list any variables you have specified at
that point in time. On the other hand, a missing log message indicates a part
of the code was skipped and never executed.
'''
import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
# ^ THis will create a LogRecord Object that will hold the information about the event
# basicConfig allows you to specify what you want to see