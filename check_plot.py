from chia.util.path import Path
from chia.plotting.check_plots import check_plots
import logging
import sys


def check_plot(challenge: int, chia_root_path: str):
    logging.basicConfig(filename='sample.log', stream=sys.stdout, level=logging.INFO)
    path = Path(chia_root_path)
    check_plots(path, challenge, None, "", True, False)
