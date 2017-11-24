import traceback
import logging

logging.basicConfig(filename='/tmp/example.log', format='%(asctime)s %(levelname)s %(message)s')

try:
    tuple()[0]
except IndexError:
    logging.error(traceback.format_exc())
    raise
