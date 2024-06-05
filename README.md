# ipynb-proj-setup

A structured IPython Notebook project with organized Python packages for enhanced data analysis.

## Getting Started

### Requirements
- Python 3.10 or higher

### Setup

1. **Create a Virtual Environment:**

   In the root directory, run:

   ```sh
   python3.10 -m venv venv
   source venv/bin/activate
   ```

2. **Install Poetry:**

   Install [Poetry](https://python-poetry.org/docs/cli/) for dependency management:

   ```sh
   venv/bin/pip install -U pip setuptools
   venv/bin/pip install poetry
   ```

3. **Install Dependencies:**

   Use Poetry to install project dependencies:

   ```sh
   poetry install --no-root
   ```

4. **Set Up Pre-Commit Hooks:**

   Install [pre-commit](https://pre-commit.ci) hooks for static tests:

   ```sh
   pre-commit install
   ```

### Running the Main Program

1. Open `main.ipynb` in Visual Studio Code.
2. Select the kernel: `venv/bin/python`.
3. Click the 'Run All' button at the top of the notebook.

### Running Unit Tests

To execute all tests, run the following command (add `-v` for verbose output):

```sh
poetry run pytest
```

### Continuous Integration

This project uses [GitHub Actions](https://docs.github.com/en/actions) for continuous integration. The CI pipeline includes:

- Building the project
- Running unit tests on every push
