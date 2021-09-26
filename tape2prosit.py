import click
from PrositTransformer.fileConverters.Tape2Prosit import Tape2Prosit
from pathlib import Path

@click.command()
@click.option('--tape_result', type=click.Path(), help="Path to tape result.")
@click.option('--prosit_hdf5_path', type=click.Path(), help="Path to prosit hdf5 path.")
@click.option('--out_path', type=click.Path(), help="Path to tape result in prosit hdf5 format.")
def cli(tape_result: Path, prosit_hdf5_path: Path, out_path: Path)->None:
    """Convert tape result into prosit hdf5-format"""
    if not out_path.endswith("/"):
        out_path += "/"

    CONVERT = Tape2Prosit.fromPath(prosit_hdf5_path, tape_result)
    CONVERT.convert(f"{out_path}tapeResult.hdf5")
