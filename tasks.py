from pathlib import Path
import shutil

from jinja2 import Template
from invoke import task
import jupytext

_TARGET = Path('~', 'dev', 'ploomber').expanduser()


@task
def setup(c, from_lock=False):
    """Create conda environment
    """
    if from_lock:
        c.run('conda env create --file environment.yml --force')
    else:
        c.run('conda env create --file environment.dev.yml --force')
        c.run('conda env export --no-build --file environment.yml'
              ' --name ploomber-workshop')


@task
def convert(c):
    """Generate README.md and index.md. Convert index.md to index.ipynb
    """
    print('Generating README.md and index.md...')
    print('Generating index.ipynb...')
    nb = jupytext.read('index.md')
    jupytext.write(nb, 'index.ipynb')

    workshop_md = _TARGET / 'workshop.md'

    img_source = '_static/workshop.svg'
    img = _TARGET / '_static' / 'workshop.svg'

    print(f'Copying README.md to {workshop_md}...')
    shutil.copy('README.md', workshop_md)
    print(f'Copying {img_source} to {img}...')
    shutil.copy(img_source, img)


@task
def clear(c):
    """Clear outputs generated when running the code
    """
    playground = Path('playground')

    if playground.exists():
        shutil.rmtree('playground')

    playground.mkdir(exist_ok=True)
    shutil.copy('_sample/nb.ipynb', 'playground/nb.ipynb')
