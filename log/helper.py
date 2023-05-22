import  logging

logger = logging.getLogger(__name__)

# create a handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.error("ERROR message")
logger.warning("warning message")



logger.info('hello from helper')