#!/usr/bin/env python3

import sys
import importlib.metadata


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_packages() -> bool:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    all_ok = True
    installed_versions: dict[str, str] = {}
    for package, description in REQUIRED_PACKAGES.items():
        try:
            version = importlib.metadata.version(package)
            installed_versions[package] = version
            print(f"[OK] {package} ({version}) - {description}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {package} - Not installed")
            all_ok = False
    if not all_ok:
        print("\nMissing dependencies detected!\n")
        print("To install using pip:")
        print("  pip install -r requirements.txt")
        print("To install using Poetry:")
        print("  poetry install\n  poetry run python loading.py")
    return all_ok


def matrix_data_analysis() -> None:
    import numpy  # type: ignore
    import pandas  # type: ignore
    import matplotlib.pyplot  # type: ignore
    print("Analyzing Matrix data...")
    data_points = 1000
    print(f"Processing {data_points} data points...")
    # generates 1000 random numbers around number 50
    matrix_signal = numpy.random.normal(loc=50, scale=10, size=data_points)
    # creates a data_frame (tabel) with all the numbers
    data_frame = pandas.DataFrame({"signal": matrix_signal})
    # calculates the average
    mean_val = data_frame["signal"].mean()
    print("Generating visualization...")
    # creates a rectangle
    matplotlib.pyplot.figure(figsize=(10, 5))
    # creates the green graphic
    matplotlib.pyplot.plot(
        data_frame["signal"],
        color="#00FF66",
        alpha=0.7,
        label="Matrix Signal"
    )
    # creates the mid red line (average)
    matplotlib.pyplot.axhline(
        mean_val,
        color="red",
        linestyle="--",
        label=f"Mean ({mean_val:.2f})",
    )
    # gives names to what we see in the image
    matplotlib.pyplot.title("Matrix Data Signal Analysis")
    matplotlib.pyplot.xlabel("Data Stream Index")
    matplotlib.pyplot.ylabel("Signal Value")
    # creates the legend rectangle
    matplotlib.pyplot.legend()
    matplotlib.pyplot.grid(True, alpha=0.2)
    # creates file and saves it
    output_filename = "matrix_analysis.png"
    matplotlib.pyplot.savefig(output_filename)
    matplotlib.pyplot.close()
    print("\nAnalysis complete!")
    print(f"Results saved to: {output_filename}")


def main() -> None:
    if not check_packages():
        sys.exit(1)
    print()
    matrix_data_analysis()


if __name__ == "__main__":
    main()
