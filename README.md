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

---

## 🚀 End-User Setup & Usage

- **Use the Makefile to create a .venv and install user-level dependencies.**

    ```bash
    make env
    ```

    This creates `.venv/` and installs packages from `requirements.txt` (if present).

- **For refreshing and installing updated dependencies, run**

    ```bash
    git pull        # get latest code + updated requirements.txt
    make install    # refresh dependencies inside .venv
    ```

- **To manually install missing packages or dependencies in the venv**

    ```sh
    source .venv/bin/activate
    pip install <package>
    ```

- **Clean build/cache files**

    ```sh
    make clean
    ```

- **Usage**



## 👤 Maintainer

**Ankit Shrivastava**
Feel free to open an issue or discussion for support.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for full details.

---

## 📈 Project Status

> Status: 🚧 In Development — Not ready for production use.

---

## 📘 References

- [Cookiecutter Docs](https://cookiecutter.readthedocs.io)
- [PEP 621](https://peps.python.org/pep-0621/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [MLOPS_example](https://github.com/gift-exe/customer-satisfaction-mlops-main)
