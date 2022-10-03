
import logging


logger = logging.getLogger(__name__)


def calculate_list_length(the_list):

    if isinstance(the_list, list):
        length = len(the_list)
    else:
        logger.error("Input needs to be a list")
        raise TypeError

    return length
