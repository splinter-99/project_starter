#!/usr/bin/python3.11
import subprocess

import click
from pathlib import Path
from subprocess import run


@click.command()
@click.option('--name', '-n', type=str, prompt='Enter project name', help='Name your project', required=True)
@click.option('--path', '-p', type=str, prompt='Specify file path for your project', help='Path where project files will be spawned', default=Path.cwd())
def project_starter(name, path):
    """
    Spawn project directory with standard project files
    1. README.md
    2. requirements.txt
    3. Create a virtual environment
    4. Create a .gitignore
    5. Initialize git and make our first commit
    """
    project_dir = Path(path) / name
    project_dir.mkdir()
    (project_dir/"README.md").touch()
    (project_dir/"requirements.txt").touch()

    # Create .gitignore and venv
    with open((project_dir/".gitignore"), mode="w") as f:
        f.write(
            "\n".join(['venv', '__pycache__', '.git'])
        )

    # Create venv and make our first commit
    cmds = [
        ['python3', '-m', 'venv', f'{project_dir}/'],
        ['git', '-C', name, 'init'],
        ['git', '-C', name, 'add', '.'],
        ['git', '-C', name, 'commit', '-m', 'Initial commit']
    ]

    for cmd in cmds:
        try:
            run(cmd, check=True, timeout=30)
        except FileNotFoundError as e:
            print(f"The program you are trying to launch can't be found\n{e}")
        except subprocess.CalledProcessError as e:
            print(f"Command failed and exited with non-zero exit status\n{e}")
        except subprocess.TimeoutExpired as e:
            print(f"Command timed out\n{e}")


if __name__ == "__main__":
    project_starter()
