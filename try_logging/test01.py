import logging
logging.basicConfig()
LOGGER = logging.getLogger(__name__)
#LOGGER.setLevel(logging.DEBUG)
LOGGER.info("info")
LOGGER.warning("Warning")
print(LOGGER.level, logging.INFO)