import logging


class CustomLogger:
    _path = "/Users/amitkumar/Documents/BACKEND-PROJ/trimble-agri/results/out.txt"

    def __init__(self, logger_name, log_file=_path):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%d-%b-%y %H-%M-%S')

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        else:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_error(self, message):
        self.logger.error(message)
