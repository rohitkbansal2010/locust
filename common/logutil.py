import logging
import socket

from logging.handlers import RotatingFileHandler


def append_file_logger():
    root_logger = logging.getLogger()
    log_format = ("%(asctime)s.%(msecs)03d000 [%(levelname)s] {0}/%(name)s: "
                  "%(message)s".format(socket.gethostname()))
    formatter = logging.Formatter(log_format, '%Y-%m-%d %H:%M:%S')
    file_handler = RotatingFileHandler('../locust.log',
                                       maxBytes=5 * 1024 * 1024,
                                       backupCount=3)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)

