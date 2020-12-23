import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs.log", format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)
        logger = logging.getLogger()
        return logger
#format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S:%P',