from chia.util.path import Path
from chia.plotting.check_plots import check_plots
import logging
from dissect_log import dissect_log


def check_plot(challenge: int, chia_root_path: str, pseudo: str):
    logging.basicConfig(filename='sample.log', filemode='w', level=logging.INFO)
    path = Path(chia_root_path)
    check_plots(path, challenge, None, "", True, False)
    dissect_log(pseudo, challenge)

