# Example Project

This is an example python project meant to serve as a testbed for any python
functionality, automatic testing, packaging, etc...

# Features

The following features are included:

- pre-commit hooks https://pre-commit.com/
- linting
  - ruff: https://github.com/astral-sh/ruff
  - pydocstyle: https://www.pydocstyle.org/en/stable/
- testing
  - pytest: https://docs.pytest.org/en/stable/
  - doctest: https://docs.python.org/3/library/doctest.html
- documentation with sphinx: https://www.sphinx-doc.org/en/master/
- python packaging
  - build: https://packaging.python.org/en/latest/tutorials/packaging-projects/
  - hatch: https://hatch.pypa.io/latest/
- example jupyter notebooks

# Developing

0. create a virtual environment

  python -m venv my_virtual_environment

1. activate the virtual environment

  cd my_virtual_environment && . bin/activate

2. install the environment

  pip install -e .

3. start developing...

# Contact

author: aetv (akke.viitanen@iki.fi)
