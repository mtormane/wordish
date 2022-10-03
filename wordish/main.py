import logging

from argparse import ArgumentParser

from wordish.text_parser import TextParser

from wordish.word_listing import create_word_list

from wordish.word_counting import calculate_list_length

file_parser = TextParser()

logger = logging.getLogger(__name__)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()


def load_data(file_path):

    logger.info("Loading database from: %s", file_path)
    file_parser.load_file(file_path)
    return file_parser.data


def main():

    logger.info("Wordish...")
    args = parse_arguments()
    text_str = load_data(args.file_path)
    word_list = create_word_list(text_str)
    length_of_words = calculate_list_length(word_list)


def init():

    if __name__ == "__main__":
        main()


init()
