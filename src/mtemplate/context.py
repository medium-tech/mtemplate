import logging
import sys


def init_logger(level=logging.INFO):
	logging.basicConfig(
		level=level,
		stream=sys.stdout,
		format="%(asctime)s %(levelname)s %(filename)s line: %(lineno)d :: %(message)s"
	)
