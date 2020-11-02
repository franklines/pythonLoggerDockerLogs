import logging
import sys

pid1stdout = open('/proc/1/fd/1','w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(pid1stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Log message sent from Python logger script to pid 1 stdout')