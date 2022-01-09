""" Global variables """
from pathlib import Path

home_dir: str = str(Path.home())
filename: str = ".tz-cli"
config_file: str = f"{home_dir}/{filename}"
