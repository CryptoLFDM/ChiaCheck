import colorlog
import logging
import re
import requests
from datetime import datetime
import time
import pytz

# Logging part
DEFAULT = 1
INFO = 2
SUCCESS = 3
HIGHLIGHT = 4
WARNING = 5
FAILED = 6
logging.addLevelName(DEFAULT, 'INFO')
logging.addLevelName(INFO, 'INFO')
logging.addLevelName(SUCCESS, 'SUCCESS')
logging.addLevelName(HIGHLIGHT, 'HIGHLIGHT')
logging.addLevelName(WARNING, 'WARNING')
logging.addLevelName(FAILED, 'FAILED')
color_mapping = {
    'DEFAULT': 'grey',
    'INFO': 'cyan',
    'SUCCESS': 'green',
    'HIGHLIGHT': 'yellow',
    'WARNING': 'purple',
    'FAILED': 'red'
}
log_pattern = '%(asctime)s %(log_color)s%(levelname)s%(reset)s | %(name)s | %(log_color)s%(message)s'
formatter = colorlog.ColoredFormatter(log_pattern, log_colors=color_mapping)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger('dissect_log')
logger.addHandler(handler)
logger.setLevel(DEFAULT)

plot_line_pattern = 'INFO:chia.plotting.check_plots:Testing plot (.*)/(plot.*.plot) k=(.*)'
plot_pool_contract_pattern = 'INFO:chia.plotting.check_plots:	Pool contract address:  (.*)'
plot_farmer_public_key_pattern = 'INFO:chia.plotting.check_plots:	Farmer public key:      (.*)'
plot_proof_result_pattern = 'INFO:chia.plotting.check_plots:	Proofs (.*) / (.*), (.*)'
summary_pattern = 'INFO:chia.plotting.check_plots:Found (.*) valid plots, total size (.*) (.*)'
summary_invalid_pattern = 'WARNING:chia.plotting.check_plots:(.*) invalid plots found:$'
invalid_plot_pattern = 'WARNING:chia.plotting.check_plots:(/.*plot-.*.plot$)'

plot_line_pattern_compiled = re.compile(plot_line_pattern)
plot_pool_contract_pattern_compiled = re.compile(plot_pool_contract_pattern)
plot_farmer_public_key_pattern_compiled = re.compile(plot_farmer_public_key_pattern)
plot_proof_result_pattern_compiled = re.compile(plot_proof_result_pattern)
summary_pattern_compiled = re.compile(summary_pattern)
summary_invalid_pattern_compiled = re.compile(summary_invalid_pattern)
invalid_plot_pattern_compiled = re.compile(invalid_plot_pattern)


def dissect_log(pseudo: str, challenge: int):
    local_logs = DissectLogs(pseudo, challenge)
    local_logs.handle_log_lines()
    local_logs.send_to_minotor()


def get_log_lines_from_logs() -> list:
    lines = []
    log_file = open('sample.log', 'r')
    log_file_content = log_file.readlines()
    for line in log_file_content:
        lines.append(line.strip())
    return lines


def create_plot_item(name: str, folder: str, size: int) -> dict:
    plot = {
        'name': name,
        'size': size,
        'folder': folder
    }
    return plot


def update_dict_with_key_value(base_dict: dict, field: str, value: any) -> dict:
    base_dict.update({field: value})
    return base_dict


class DissectLogs:
    def __init__(self, pseudo, challenge):
        self.pseudo = pseudo
        self.challenge = challenge

    file_content = get_log_lines_from_logs()
    plots = []
    current_plot = {}
    farm_summary = {}
    invalid_plots = []
    ac_file_path = 'ssl/chain.pem'

    def send_to_minotor(self):
        resp = requests.post(url='http://minotor-alpha.ether-source.fr:8080/chia/plot_check_summary',
                             json=self.create_summary(),
                             verify=self.ac_file_path)
        logger.log(INFO, 'Data sent to minotor with code {} and message: {}'.format(resp.status_code, resp.text))

    def handle_log_lines(self):
        for line in self.file_content:
            self.handle_plot_metadata(line)
            self.handle_contract_pool(line)
            self.handle_farmer_key(line)
            self.handle_proof(line)
            self.handle_summary(line)
            self.handle_summary_invalid(line)
            self.handle_invalid_plot(line)
        logger.log(HIGHLIGHT,
                   'See result on https://mythologic.fr/d/k9v1FlP4z/chia-plot-check-summary?orgId=7&var-Pseudo={}&refresh=30s'.format(
                       self.pseudo))

    def handle_plot_metadata(self, line: str):
        if plot_line_pattern_compiled.match(line):
            if self.current_plot != {}:
                self.plots.append(self.current_plot)
            self.current_plot = {}
            search = re.search(plot_line_pattern, line)
            logger.log(INFO, 'going to test plot size k{} in {} with name {}'.format(search.group(3), search.group(1),
                                                                                     search.group(2)))
            self.current_plot = create_plot_item(search.group(2), search.group(1), int(search.group(3)))

    def handle_contract_pool(self, line: str):
        if plot_pool_contract_pattern_compiled.match(line):
            search = re.search(plot_pool_contract_pattern, line)
            logger.log(INFO, '{} is having {} contract pool'.format(self.current_plot['name'], search.group(1)))
            self.current_plot = update_dict_with_key_value(self.current_plot, 'contract_pool', search.group(1))

    def handle_farmer_key(self, line: str):
        if plot_farmer_public_key_pattern_compiled.match(line):
            search = re.search(plot_farmer_public_key_pattern, line)
            logger.log(INFO, '{} is having {} farmer key'.format(self.current_plot['name'], search.group(1)))
            self.current_plot = update_dict_with_key_value(self.current_plot, 'farmer_key', search.group(1))

    def handle_proof(self, line: str):
        if plot_proof_result_pattern_compiled.match(line):
            search = re.search(plot_proof_result_pattern, line)
            if float(search.group(3)) > 0.8:
                color = SUCCESS
            else:
                color = FAILED
            logger.log(color,
                       '{} is having {} quality with score {} / {}'.format(self.current_plot['name'],
                                                                           search.group(3),
                                                                           search.group(1),
                                                                           search.group(2)))
            self.current_plot = update_dict_with_key_value(self.current_plot, 'plot_quality', float(search.group(3)))
            self.current_plot = update_dict_with_key_value(self.current_plot, 'proof_found', int(search.group(1)))
            self.current_plot = update_dict_with_key_value(self.current_plot, 'proof_tested', int(search.group(2)))

    def handle_summary(self, line: str):
        if summary_pattern_compiled.match(line):
            search = re.search(summary_pattern, line)
            logger.log(SUCCESS, '{} plots found => {} {}'.format(search.group(1), search.group(2), search.group(3)))
            self.farm_summary = {'plots_count': int(search.group(1)), 'plots_size': float(search.group(2)),
                                 'plots_size_unit': search.group(3)}

    def handle_summary_invalid(self, line: str):
        if summary_invalid_pattern_compiled.match(line):
            search = re.search(summary_invalid_pattern, line)
            logger.log(WARNING, '{} invalid plots found '.format(search.group(1)))
            self.farm_summary = update_dict_with_key_value(self.farm_summary, 'invalid_plots_count',
                                                           int(search.group(1)))

    def handle_invalid_plot(self, line: str):
        if invalid_plot_pattern_compiled.match(line):
            search = re.search(invalid_plot_pattern, line)
            logger.log(FAILED, '{} is invalid '.format(search.group(1)))
            self.invalid_plots.append(search.group(1))

    def create_summary(self) -> dict:
        plot_check_sumarry = {
            'plots': self.plots,
            'invalid_plots': self.invalid_plots,
            'pseudo': self.pseudo,
            'farm_summary': self.farm_summary,
            '@timestamp': datetime.fromtimestamp(time.time(), pytz.UTC).isoformat(),
            'challenge': self.challenge
        }
        return plot_check_sumarry
