import logging 
import pathlib

audit_dir = pathlib.Path('logs') 
audit_dir.mkdir(exist_ok=True)

log_file = audit_dir/ 'suite.log'

logger = logging.getLogger('TTechLogger')
logger.setLevel(logging.INFO)

if not logger.hasHandlers:
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(astime)s %(levelname)s %(name)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


