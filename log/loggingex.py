import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')


logging.debug("this is debug msg")
logging.info("this is info msg")
logging.warning("this is warn msg")
logging.error("this is error msg")
logging.critical("this is critical msg")

import helper