"""Argument parsing and YAML-based configuration utilities."""

import argparse
from typing import Any

from ruamel import yaml


class AttrDict(dict[str, Any]):
    """Dictionary with attribute-style access (recursive)."""

    def __getattr__(self, key: str) -> Any:
        try:
            value = self[key]
        except KeyError as e:
            raise AttributeError(key) from e

        if isinstance(value, dict) and not isinstance(value, AttrDict):
            value = AttrDict(value)
            self[key] = value
        return value

    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

    def __delattr__(self, key: str) -> None:
        try:
            del self[key]
        except KeyError as e:
            raise AttributeError(key) from e


def parse_arguments(hyperparameters):
    """Parse command-line arguments overriding given hyperparameters."""
    parser = argparse.ArgumentParser(description="Hyperparameters")

    def _infer_list_type(sample):
        """Infer the element type for a list-valued hyperparameter."""
        if not sample:
            return str
        return type(sample[0])

    for key, value in hyperparameters.items():
        if isinstance(value, bool):
            parser.add_argument(f"--{key}", action="store_true", default=value)
        elif isinstance(value, list):
            parser.add_argument(
                f"--{key}",
                nargs="+",
                type=_infer_list_type(value),
                default=value,
            )
        else:
            parser.add_argument(f"--{key}", type=type(value), default=value)
    args = parser.parse_args()
    return vars(args)


def get_configuration(yaml_file):
    """Load hyperparameters from YAML and merge with CLI overrides."""
    with open(yaml_file, "r", encoding="utf-8") as f:
        yaml_loader = yaml.YAML()
        hyperparameters = yaml_loader.load(f)

    def _convert_value(v):
        """Convert YAML string values to appropriate data types."""
        if isinstance(v, str):
            if v.lower() in {"true", "false"}:
                return v.lower() == "true"
            try:
                if "." in v:
                    # Convert to float if it contains a decimal
                    # Convert to int if no decimal
                    return float(v)
                return int(v)
            except ValueError:
                # Keep as string if conversion fails
                return v
        # Return as-is if not a string
        return v

    for key, value in hyperparameters.items():
        hyperparameters[key] = _convert_value(value)

    hyperparameters.update(parse_arguments(hyperparameters))
    return AttrDict(hyperparameters)
