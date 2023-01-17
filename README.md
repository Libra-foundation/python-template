# Python Template

This repository contains various templates for as many python projects as we could. We currently only have a template for general purpose python project/library.

We also planed some other specialized templates like a django template wich should be comming soon.

## How to use ?

First simply click on the "use this template" button that should be somewhere in the UI :).
We decided to use `anaconda` with `poetry` for the dependencies management if you never used them before you'll see how much it will change your life.

### Setup
You will first need to install Conda. You can find the documentation about this installation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). As of the latest update of this documentation, Conda version `22.11.0` was used. Feel free to give feedback about the installation process with newer version of Conda.

Once Conda is installed, and your new repository cloned on your machine,  open your command prompt in the root folder of the repository. Then, run the following commands :

 - `conda env create -f environment.yml -p ./venv`
 - `conda activate ./venv`
 - `poetry install --with dev`
 - `pre-commit install --install-hooks`

 And you are ready to start your project !

We recommand you give a quick read to the [poetry's CLI documentation](https://python-poetry.org/docs/cli/) just to at least know how to add new dependencies.


### Features and daily usage
This template includes two really useful tools:

 - [pre-commit](https://github.com/pre-commit/pre-commit)
 - [poethepoet](https://github.com/nat-n/poethepoet)

`pre-commit` allow you to run automatic commands before commiting. By default this template will export the dependencies in the pip format (this makes the creation of workflow and the deployment of apps easier), format the code using `autopep8` and will sort your imports thanks to `isort`

`poethepoet` allow us to define usefull commands for you to use. We currently define 4 commands:
 - `poe lint [files]` : will pass your files through MyPy, Pylint and bandit, all of which have been pre-configured by ourselfs. This command will tell you were types are missing and show you potential future problems to help you produce your best code.
 - `poe test` : This command will run all tests. This template uses pytest with few plugins, one might interest you in particular : [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/latest/usage.html). This plugin allow you, if needed, to benchmark your project while testing it. This can be especially usefull if you need to monitor the performance of your application.
 - `poe coverage` : This command will produce a coverage report. It will help you diagnose wich part of your application isn't well covered by your tests. Since we need to run all tests to compute the coverage, the benchmarks have been disabled when running this particular command.


