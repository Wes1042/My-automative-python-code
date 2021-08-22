Levels of logging

There are multiple levels to logging

The common use of logging used is :
logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s - (levelname)s - %(message)s')

                Table 10-1. Logging Levels in Python
Level       Logging Function                Description

DEBUG       logging.debug()                 The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO        logging.info()                  Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING     logging.warning()               Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR       logging.error()                 Used to record an error that caused the program to fail to do something.

CRITICAL    logging.critical()              The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.