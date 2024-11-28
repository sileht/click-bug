import click


@click.command()
@click.option(
    "--verbose",
    "-v",
    default=False,
    is_flag=True,
)
def work(verbose: bool) -> None:
    print(verbose)


@click.command()
@click.option(
    "--verbose",
    "-v",
    default=lambda: False,
    is_flag=True,
)
def buggy(verbose: bool) -> None:
    print(verbose)


@click.group()
def cli() -> None:
    pass


cli.add_command(work)
cli.add_command(buggy)

cli()
