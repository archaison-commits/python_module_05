#!/usr/bin/env python3

import importlib


if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...\n")
    dependencies = ["pandas", "numpy"]
    descriptions = {
        "pandas": " - Data manipulation ready",
        "numpy": " - Numerical computation ready"}
    print("Checking dependencies:")
    missing_dep = []
    from importlib.metadata import version
    from importlib.metadata import PackageNotFoundError
    for i in dependencies:
        try:
            module = importlib.import_module(i)
            package_version = version(i)
        except (ImportError, PackageNotFoundError):
            print(f"[KO] {i} - Not installed")
            missing_dep.append(i)
        else:
            print(f"[OK] {module.__name__} ({package_version}){(descriptions[i])}")
            # print(package_version)
            # print(module.__name__)
    if missing_dep:
        print("\nSome dependencies are missing.\n")
        for missing in missing_dep:
            print(f"To install {missing}:\n"
                  f"pip: python3 -m pip install {missing}\n"
                  f"poetry: poetry add {missing}\n")
    else:
        print("\nAll reagents loaded successfully.")

