# supop-pai-cookiecuttter-template

A cookiecutter template that you can use to start your project.

This template is part of a lecture given at [Institut d'Optique](https://www.institutoptique.fr/).
Students are expected to use last good practice coding tools, including cookiecutter. This template will help them get started with everything installed.

See official website (in French) : https://sites.google.com/view/supop-pai

## Features

- NiceGUI basic app
- QT basic app
- Docs website with sphinx
- pre-commit linting
- pyright type checking
- Unit tests with pytest
- Github CI that will run pre-commit, pytest and pyright for each pushed commit
- Issue and Pull Request templates

## How to use

The following indications assume you have `uv` and `git` installed and usable within your terminal.
See [Install instructions](https://docs.astral.sh/uv/getting-started/installation/).

1. Create your own repo on github, keep it empty. Optionally, add a License (this template does not have any).
2. Clone it, and note the github web address to your repo (not the git address).
3. Enter your newly cloned (and empty) repository and from there call the following command

    ```bash
    uvx cookiecutter https://github.com/ClementPinard/supop-pai-cookiecuttter-template
    ```

    It will ask for:

    - The project name
    - the repo name: make it so it matches the repo name on github
    - the github web adress of your project

    Your project squeleton is generated directly inside your repository.

4. You can now commit and push to have a first version of your project

    ```bash
    git add .
    git commit -m "First commit applying template"
    git push
    ```

5. Notice the github actions on your repository.

    Several tests should have been started:

    - Pre-commit linting
    - Pyright type-checking
    - Tests (with pytest and coverage)
    - Documentation building

    They will run each time you push a commit. Use them to make sure your project stay
    at the same quality level throughout development.

    To customize them, you can modify the `.github/workflows/CI.yaml` file in your repo.

6. Start coding !

    - Use the already built-in examples to either construct a Qt app or a NiceGUI app
    - Don't forget to implement tests as you add features.
    - Don't forget to have an up to date README on how to install and use your app.
    - Even better if you are able to construct a good documentation website.
      The pre-built documentation website will look at the docstrings in your code and
      create an index with them. The function in `typed_function` in the `my_module.py`
      file has been extensively typed and documented to show you how it looks like.
