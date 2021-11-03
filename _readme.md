# Ploomber Workshop Material

Authors: [Eduardo Blancas](https://twitter.com/edublancas) and [Ido Michael](https://www.linkedin.com/in/ido-michael/)

This workshop demonstrates how to develop reproducible pipelines using [Ploomber](https://github.com/ploomber/ploomber).

To start, [click here](https://mybinder.org/v2/gh/edublancas/ploomber-workshop/main?urlpath=lab/tree/index.ipynb) or on the button below:

<p align="center">
  <a href="https://mybinder.org/v2/gh/edublancas/ploomber-workshop/main?urlpath=lab/tree/index.ipynb"> <img src="_static/workshop.svg" alt="Start Workshop"> </a>
</p>

**Note:** It may take a few seconds for the notebook to load.

If you prefer to run things locally, scroll down to the *Running it locally* section.

## Workshop level: intermediate

## Background knowledge

Familiarity with JupyterLab, and a basic knowledge of pandas.

## Workshop content

1. What is Ploomber?
2. Describing a pipeline using a `pipeline.yaml` file
3. Describing tasks
4. Scripts as notebooks, and notebooks as outputs
5. Scaffolding projects
6. Adding task dependencies
7. Pipeline visualization
8. Coding the analysis
9. Incremental builds

[Documentation](https://ploomber.readthedocs.io/en/latest/get-started/index.html)

## Format

1. 60-minute session

## Running it locally (with conda)

You can also follow this workshop locally, but it requires a bit more setup:

Pre-requisites:

1. [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. `git`

```sh
# clone the repository
git clone https://github.com/edublancas/ploomber-workshop
cd ploomber-workshop

# install dependencies (requires conda)
pip install invoke
invoke setup --from-lock

# activate environment
conda activate ploomber-workshop

# start jupyter
jupyter lab
```

Then open `index.ipynb`.

## Running it locally (with pip)

```sh
# install dependencies
pip install --upgrade pip
pip install -r requirements.dev.txt

# start jupyter
jupyter lab
```

Then open `index.ipynb`.

## Support us

If you like our project, please give us a ⭐️ on [GitHub](https://github.com/ploomber/ploomber).

## Contact

* [Join our community](http://community.ploomber.io)
* E-mail: [contact@ploomber.io](mailto:contact@ploomber.io)
* [Twitter](https://twitter.com/ploomber)
