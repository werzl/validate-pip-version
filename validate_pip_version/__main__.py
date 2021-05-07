import sys
import os
import click
import importlib.metadata
from packaging import version


class Checker:
    def __init__(self, package_name: str):
        self.cwd = os.getcwd()
        self.package_name = package_name

    def strip_version_from_init_file(self, file_path: str) -> str:
        new_version = ""

        with open(os.path.join(self.cwd, file_path)) as f:
            for line in f:
                if line.startswith("__version__"):
                    _, _, new_version = line.replace(
                        "\"", "").replace("\'", "").replace("\"", "").split()
                    break

        if new_version == "":
            raise Exception(f"Couldn't find version in: {file_path}")

        return new_version

    def strip_version_from_setup_file(self, file_path: str) -> str:
        matcher = "version="
        new_version = ""

        with open(os.path.join(self.cwd, file_path)) as f:
            for line in f:
                if "version=" in line:
                    # Strip quotes and commas
                    new_version = line.replace(matcher, "").replace(
                        "\"", "").replace("\'", "").replace(",", "")

                    # Strip trailing /n and spaces
                    new_version = new_version.rstrip().strip()
                    break

        if new_version == "":
            raise Exception(f"Couldn't find version in: {file_path}")

        return new_version

    def compare_version(self, new_version: str):
        try:
            new_version = version.parse(new_version)
            current_version = version.parse(
                importlib.metadata.version(self.package_name))

            if new_version > current_version:
                click.echo(
                    f"Version: {new_version} is valid. (Current version: {current_version})")
            else:
                if new_version == current_version:
                    click.echo(
                        f"Version: {str(new_version)} can't be the same as the current version ({str(current_version)})")
                if new_version < current_version:
                    click.echo(
                        f"Version: {str(new_version)} can't be lower than the current version ({str(current_version)})")

                sys.exit(1)

        except Exception as e:
            click.echo(
                f"Error parsing versions -- New Version: {str(new_version)} -- Current Version: {str(current_version)} -- Error: {e}")
            raise e


@click.group()
def cli():
    pass


@cli.command()
@click.option("--package_name", "-n", required=True, help="Name of the package on PyPi")
@click.option("--setup_file_path", required=True, help="Relative file path for the setup.py file (uses current working dir)")
def check_setup_file(package_name: str, setup_file_path: str):
    checker = Checker(package_name)

    new_version = checker.strip_version_from_setup_file(setup_file_path)

    checker.compare_version(new_version)


@cli.command()
@click.option("--package_name", "-n", required=True, help="Name of the package on PyPi")
@click.option("--init_file_path", required=True, help="Relative file path for the __init__.py file (uses current working dir)")
def check_init_file(package_name: str, init_file_path: str):
    checker = Checker(package_name)

    new_version = checker.strip_version_from_init_file(init_file_path)

    checker.compare_version(new_version)


if __name__ == "__main__":
    cli()
