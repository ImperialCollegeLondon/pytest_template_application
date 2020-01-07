# Python Application Template

![build status](../../workflows/ci/badge.svg)

This is a minimal Python 3 application with automated tests using [pytest](https://pytest.org/), [Coverage.py](https://coverage.readthedocs.io/) and [GitHub Actions](https://github.com/features/actions). It also provides [pre-commit](https://pre-commit.com/) hooks (for [Black](https://black.readthedocs.io/en/stable/), [reorder_python_imports](https://github.com/asottile/reorder_python_imports), [Flake8](https://flake8.pycqa.org/en/latest/) and [Mypy](http://mypy-lang.org/)) and automated Docker image storage via [GitHub Packages](https://help.github.com/en/packages). It was developed by the [Imperial College Research Computing Service](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/) for the [Essential Software Engineering for Researchers](https://imperialcollegelondon.github.io/grad_school_software_engineering_course/) course.

To use this repository as a template for your own application:

1. Click the green "Use this template" button above
1. Name and create your repository
1. Clone your new repository and make it your working directory
1. Set up a virtual environment:

   ```sh
   # Either using venv:
   python3 -m venv .venv
   source .venv/bin/activate  # or `.venv\Scripts\activate.bat` if you're using Windows
   python -m pip install -U pip
   python -m pip install -U -r requirements-dev.txt

   # Or using conda:
   conda env create --name my_application --file requirements-dev.txt python=3
   conda activate my_application
   ```

1. Install the git hooks:

   ```sh
   pre-commit install
   ```

1. Run the tests:

   ```sh
   python -m pytest
   ```

1. Edit/replace `fibonacci.py`, `test_fibonacci.py`, `setup.cfg` and `ci.yml` as required
