import yaml
import logging.config
import os


def setup_logging(default_path='log.yaml', default_level=logging.INFO):
    """
    Setup logging configuration
    """
    if os.path.exists("mylog"):
        pass
    else:
        os.mkdir('mylog')
    path = default_path
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read(),  Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        print('the input path doesn\'t exist')


setup_logging(default_path='./log.yaml')
logger = logging.getLogger()
