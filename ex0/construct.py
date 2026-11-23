#!/usr/bin/env python3


import sys
import os
import site


if __name__ == "__main__":
    environment_name: str = os.path.basename(sys.prefix)
    if sys.prefix != sys.base_prefix:
        print("\nLABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current python: {sys.prefix}")
        print(f"Virtual Environment: {environment_name}\n")
        print("SUCCESS: you are working in an isolated environment!\n"
              "Safe to install reagents without affecting\nthe global system."
              "Reagent installationg path:")
        print(f"{site.getsitepackages()[0]}")

    else:
        print("\nLABORATORY STATUS: You are working in the open\n")
        print(f"Current python: {sys.prefix}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!\n"
              "Every reagent you install here leaks into the whole system\n")
        print("To seal the laboratory, run:\n"
              "python3 -m venv lab_env\nsource lab_env/bin/activate"
              " # On Unix\nlab_env\\Scripts\\activate #On Windows\n"
              "\nThen run this program again")
