import logging



logger = logging.getLogger(__name__)


class TextParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open the json file
        # load the json file and save it to self.data
        try:
            with open(file_path, "r", encoding="utf-8") as my_file:
                self.data = my_file.read()

            logger.info("Following data is found in the text file")
            print(self.data)



        except UnicodeDecodeError as err:
            logger.exception(err)
            raise err
