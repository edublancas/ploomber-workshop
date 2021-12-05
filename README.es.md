## ¡Muestra tu apoyo con una ⭐️ en el repositorio!

---


# Taller de Ploomber

Autores: [Eduardo Blancas](https://twitter.com/edublancas), [Ido Michael](https://www.linkedin.com/in/ido-michael/).

Este taller muestra como desarrollar pipelines de datos con [Ploomber](https://github.com/ploomber/ploomber).

Para empezar, [click aquí](https://mybinder.org/v2/gh/edublancas/ploomber-workshop/main?urlpath=lab/tree/index.es.ipynb) o en el botón a continuación:

<p align="center">
  <a href="https://mybinder.org/v2/gh/edublancas/ploomber-workshop/main?urlpath=lab/tree/index.es.ipynb"> <img src="_static/workshop.es.svg" alt="Empezar taller"> </a>
</p>

**Note:** El material tomará algunos minutos para estar listo.

Vaya a la sección *Correr localmente* si prefieres seguir el taller de manera local.

## Nivel: Intermedio

## Requisitos

Familiaridad con JupyterLab así como con pandas y scikit-learn.

## Contenido

1. Introducción
2. Refactorización de un cuaderno existente
3. El archivo `pipeline.yaml`
4. Ejecutando el pipeline
5. Declarando dependencies
6. Agregando una nueva tarea
7. Ejecuciones incrementales
8. Ejecución en la nube

[Documentación](https://ploomber.readthedocs.io/en/latest/get-started/index.html)


## Correr localmente (conda)

Pre-requisitos:

1. [miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. `git`

```sh
# clonar repo
git clone https://github.com/edublancas/ploomber-workshop
cd ploomber-workshop

# instalar dependencies (requiere conda)
pip install invoke
invoke setup --from-lock

# activar ambiente
conda activate ploomber-workshop

# iniciar jupyter
jupyter lab
```

Abre el archivo `index.es.ipynb`.

## Correr localmente (pip)

```sh
# instalar dependencies
pip install --upgrade pip
pip install -r requirements.dev.txt

# comenzar jupyter
jupyter lab
```

Abre el archivo `index.es.ipynb`.

## Apóyanos

Si te gusta nuestro proyecto, danos una ⭐️ en [GitHub](https://github.com/ploomber/ploomber).

## Contacto

* [Únete a nuestra comunidad](http://community.ploomber.io)
* E-mail: [contact@ploomber.io](mailto:contact@ploomber.io)
* [Twitter](https://twitter.com/ploomber)
