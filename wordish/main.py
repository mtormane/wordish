from argparse import ArgumentParser

import logging

from wordish.json_parser import JsonParser

file_parser = JsonParser()

logger = logging.getLogger(__name__)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()


def load_data(file_path):

    logger.info("Loading database from: %s", file_path)
    file_parser.load_file(file_path)


def main():

    logger.info("Wordish...")
    args = parse_arguments()
    load_data(args.file_path)


def init():

    if __name__ == "__main__":
        main()


init()
