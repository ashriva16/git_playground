# MLOPS Playground

<p align="left">
  <a href="https://opensource.org/licenses/MIT">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <img alt="Python Version" src="https://img.shields.io/badge/python-3.8%2B-blue" />
  <img alt="Repo Size" src="https://img.shields.io/github/repo-size/ashriva16/mlops_playground" />
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/ashriva16/mlops_playground" />
  <a href="https://github.com/ashriva16/mlops_playground/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/ashriva16/mlops_playground" />
  </a>
  <a href="https://github.com/ashriva16/mlops_playground/pulls">
    <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/ashriva16/mlops_playground" />
  </a>
  <a href="https://github.com/ashriva16/mlops_playground/actions/workflows/ci.yml">
    <img alt="CI" src="https://github.com/ashriva16/mlops_playground/actions/workflows/ci.yml/badge.svg" />
  </a>
  <a href="https://github.com/ashriva16/mlops_playground/actions/workflows/doc.yml">
    <img alt="CI" src="https://github.com/ashriva16/mlops_playground/actions/workflows/doc.yml/badge.svg" />
  </a>
</p>


## 📌 Overview

A lightweight MLOps playground focused on practicing end-to-end workflows for deployment and production.
Covers reproducible environments, experiment execution, packaging, automation, and CI/CD fundamentals.

### ✨ Features

---

## 📁 Repository Setup

```sh
git clone https://github.com/<username>/<repo>.git
cd <repo>
```

If you need a specific version:

```sh
git checkout vX.Y.Z
```

## 🧱 Project Structure

```text
├── VERSION                  # Current project version (e.g., 0.1.0)
├── CHANGELOG.md             # Chronological change history
├── requirements.txt         # End-user dependencies
├── requirements-lock.txt    # Frozen dependency set for reproducibility
├── LICENSE                  # Project license
├── Makefile                 # End-user automation commands
├── pyproject.toml           # Build system, metadata, deps, lint/format config
├── README.md                # Project overview and usage guide
│
├── docs/                              # Sphinx/MkDocs documentation
│   ├── _build/
│   │   └── html/                      # Generated HTML output
│   ├── make.bat                       # Windows build helper
│   ├── Makefile                       # Sphinx makefile for docs
│   └── source/
│       ├── api/                       # API auto-docs
│       ├── conf.py                    # Sphinx configuration
│       ├── index.rst                  # Docs entry point
│       └── _templates/                # HTML/Jinja templates
│
├── playground/              # Scratchpad; not part of production pipeline
├── src/                     # Production-grade code; packaged via pyproject.toml.
├── utils/                   # Shared utilities used across the project consider merging into src/ if used by package.
└── .github/
    └── workflows/           # CI/CD pipelines
        ├── docs.yml         # Docs build/deploy CI
        └── main.yml         # Main CI (lint, test, build)
```

## 🚀 End-User Setup & Usage

- **Use the Makefile to create a .venv and install user-level dependencies.**

    ```bash
    make env
    ```

    This creates `.venv/` and installs packages from `requirements.txt` (if present).

- **For refreshing and installing updated dependencies run**

    ```bash
    git pull        # get latest code + updated requirements.txt
    make install    # refresh dependencies inside .venv
    ```

- **To manually install packages or missing dependency in the venv**

    ```sh
    source .venv/bin/activate
    pip install <package>
    ```

- **Clean build/cache files**

    ```sh
    make clean
    ```

- **Usage**

    ```sh
    .venv/bin/python main.py
    ```

## 🤝 Contributing

Contributions are encouraged and appreciated. To maintain a clean history, all changes must be made on feature branches (direct pushes to main may be restricted).

### Setup

```sh
python3 -m venv .venv
pip install --upgrade pip
source .venv/bin/activate
pip install -e ".[dev,docs]"
```

This installs:

- the project in editable mode
- dev tools (pytest, black, isort, flake8, pylint)
- docs tools (sphinx, myst-parser, nbsphinx, etc.)

### Workflow

- To get started:

```sh
source .venv/bin/activate
# Make sure main is up to date
git checkout main
git pull --rebase
# Create a feature branch
git checkout -b <feature-name>
```

- Optional but recommended checks:

```sh
pytest
black <files>
isort <files>
flake8 <files>
```

- To apply changes:

```sh
# Stage and commit
git add <files...>
git commit -m "feat: short description"
# Push the feature branch and open a PR
git push -u origin <feature-name>
```

PR will be reviewed by admin as soon as possible.

## 👤 Maintainer

**Ankit Shrivastava**
Feel free to open an issue or discussion for support.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for full details.

## Project Status

> Status: 🚧 In Development — Not ready for production use.

## 📘 References

- [Cookiecutter Docs](https://cookiecutter.readthedocs.io)
- [PEP 621](https://peps.python.org/pep-0621/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [MLOPS_example](https://github.com/gift-exe/customer-satisfaction-mlops-main)
