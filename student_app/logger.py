'''from logging import *
LOG_FORMAT='{lineno}*******{asctime} ********** {message} '
basicConfig(filename='logfile.log',level=DEBUG,filemode='w',style='{',format=LOG_FORMAT)

logger=getLogger()

logger.debug("this is debug in w mode")
logger.info("this is info")

logger.warning("This is Warning")
logger.error("This is error")
logger.critical("thisis critical")
'''


import logging

# Use the logger defined in settings.py
logger = logging.getLogger('student_app')

from functools import wraps
from rest_framework.response import Response

def api_logger(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.info(f"API called: {request.method} {request.path}")
        logger.info(f"Request data: {request.data}")
        try:
            response = func(request, *args, **kwargs)
            if isinstance(response, Response):
                logger.info(f"Response status: {response.status_code}")
                logger.info(f"Response data: {response.data}")
            return response
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
            raise
    return wrapper
