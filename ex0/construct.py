#!/usr/bin/env python3

from site import getsitepackages
import sys
import os


def virtual_check() -> None:
    here: str = sys.prefix
    path: str = sys.base_prefix
    python_version: str = sys.executable
    if here == path:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {python_version}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        venv: str = os.path.basename(here)
        package_path: str = getsitepackages()[0]
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {python_version}")
        print(f"Virtual Environment: {venv}")
        print(f"Environment Path: {here}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(f"{package_path}")


def main() -> None:
    virtual_check()


if __name__ == "__main__":
    main()
