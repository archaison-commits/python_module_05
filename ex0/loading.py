#!/usr/bin/env python3

import importlib
from importlib.metadata import version
from importlib.metadata import PackageNotFoundError


if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...\n")
    dependencies = ["pandas", "numpy"]
    descriptions = {
        "pandas": " - Data manipulation ready",
        "numpy": " - Numerical computation ready"}
    print("Checking dependencies:")
    missing_dep = []
    for i in dependencies:
        try:
            module = importlib.import_module(i)
            package_version = version(i)
        except (ImportError, PackageNotFoundError):
            print(f"[KO] {i} - Not installed")
            missing_dep.append(i)
        else:
            print(f"[OK] {module.__name__} "
                  f"({package_version}){(descriptions[i])}")
            # print(package_version)
            # print(module.__name__)
    print("\npip vs Poetry:\n"
          "  requirements.txt declares what to install"
          "; pip resolves it at install time.\n"
          "  pyproject.toml delcares the same constraints, and "
          "Poetry pins the resolved\n  versions in poetry.lock "
          "so every install is identical.")
    if missing_dep:
        print("\nSome dependencies are missing.\n")
        for missing in missing_dep:
            print(f"To install {missing}:\n"
                  f"pip: python3 -m pip install {missing}\n"
                  f"poetry: poetry add {missing}\n")
    else:
        print("\nAll reagents present and accounted for.")
