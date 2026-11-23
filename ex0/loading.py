#!/usr/bin/env python3

import importlib


if __name__ == "__main__":
    dependencies = ["pandas", "numpy"]
    for i in dependencies:
        module = importlib.import_module(i)
        print(module.__name__)

