from pathlib import Path
import shutil

from invoke import task

import jupytext


@task
def setup(c):
    """Create conda environment
    """
    c.run('conda env create --file environment.dev.yml --force')
    c.run('conda env export --no-build --file environment.yml'
          ' --name scipy-2021')


@task
def convert(c):
    """Convert index.md to index.ipynb
    """
    nb = jupytext.read('index.md')
    jupytext.write(nb, 'index.ipynb')


@task
def clear(c):
    """Clear outputs generated when running the code
    """
    playground = Path('playground')

    if playground.exists():
        shutil.rmtree('playground')

    playground.mkdir()
    scripts = playground / 'scripts'
    scripts.mkdir()
    out = playground / 'output'
    out.mkdir()

    (playground / '.gitkeep').touch()
    (playground / 'pipeline.yaml').touch()
    (out / '.gitkeep').touch()
    (scripts / '.gitkeep').touch()

    example_out = Path('example', 'output')

    if example_out.exists():
        shutil.rmtree(example_out)

    example_out.mkdir(parents=True)