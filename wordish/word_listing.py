import logging

logger = logging.getLogger(__name__)


def create_word_list(text_str):

    if isinstance(text_str, str):
        word_list = list(text_str.split(" "))
    else:
        logger.error("Input needs to be a string")
        raise TypeError

    return word_list
