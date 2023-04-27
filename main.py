import click
from check_plot import check_plot


@click.command()
@click.option("--pseudo", required=True, help="Pseudo to search on grafana", type=str)
@click.option("--chia_root_path", required=True, help="chia root path", type=str)
@click.option("--challenge", default=32, help="The number of challenge for each plot", type=int)
def main(pseudo, challenge, chia_root_path):
    check_plot(challenge, chia_root_path, pseudo)


if __name__ == '__main__':
    main()

