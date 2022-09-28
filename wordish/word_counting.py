
import logging


logger = logging.getLogger(__name__)


def calculate_list_length(lista):

    if isinstance(lista, list):
        length = len(lista)
    else:
        logger.error("Input needs to be a list")
        raise TypeError

    return length
