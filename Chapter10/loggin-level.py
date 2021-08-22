import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# THis is setting the levels of logging that can be used in your program
logging.debug('some debugging details')

logging.info('The logging module is working')

logging.warning('An error message is about to be logged')

logging.critical('The program is unable to recover!')

#----------------------------------------
'''Disabling loggin'''
logging.basicConfig(level=logging.INFO,format='%(asctime)s -%(levelname)s - %(message)s')

logging.critical('Critical erros! Critical error')
logging.disable(logging.CRITICAL) # after it has been disbale it will not appears
logging.critical('Critical error! Critical error!')
logging.error('Error! Error')

# To disable it in the whole program you will write it next to import logging

'''Logging to a File'''
#Instead of writting to the console we can set it up for a file
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.error('Error! Error')
