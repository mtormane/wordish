import json
import logging


logger = logging.getLogger(__name__)


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open the json file
        # load the json file and save it to self.data
        try:
            with open(file_path, "r") as my_file:
                self.data = json.loads(my_file.read())
            logger.info("Following data is found in the json file")
            for keys in self.data:
                tmp_dict = self.data[keys]
                logger.info("Data container %s contains", keys)
                logger.info("%s", tmp_dict)

        except (ValueError) as err:
            logger.exception(err)
            raise err
