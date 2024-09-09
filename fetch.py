#!/usr/bin/python3

import os
import subprocess
import zipfile
import shutil
from pathlib import Path


# Function to download and extract a package from PyPI
def fetch_package(package_name, target_dir="downloaded_package"):
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)
    # Step 1: Use pip to download the package
    print(f"Downloading {package_name}...")
    subprocess.run(
        ["pip", "download", "--no-deps", "--dest", target_dir, package_name], check=True
    )
    # convert kebab to camel for wheels
    pythonic_package_name = package_name.replace("-", "_")
    # Find the downloaded package file (should be a .tar.gz or .whl)
    downloaded_files = list(Path(target_dir).glob(f"{pythonic_package_name}*"))
    if not downloaded_files:
        raise FileNotFoundError(
            f"Package {pythonic_package_name} not found in {target_dir}"
        )

    package_file = downloaded_files[0]
    print(f"Package file: {package_file}")
    # Step 2: Extract the package contents
    extract_dir = os.path.join(target_dir, "extracted")
    os.makedirs(extract_dir, exist_ok=True)
    if package_file.suffix == ".whl":
        with zipfile.ZipFile(package_file, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
    else:
        shutil.unpack_archive(str(package_file), extract_dir)
    return extract_dir


# Function to find HTML/web assets in the extracted package
def find_web_assets(extract_dir):
    web_assets = []
    for root, _, files in os.walk(extract_dir):
        for file in files:
            if file.endswith((".html", ".css", ".js")):
                web_assets.append(os.path.join(root, file))
    return web_assets


if __name__ == "__main__":
    import argparse

    # Step 1: Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Fetch a package from PyPI and extract its web assets."
    )
    parser.add_argument(
        "package_name", type=str, help="Name of the package to fetch from PyPI"
    )
    args = parser.parse_args()
    package_name = args.package_name
    # Step 1: Fetch and extract the package
    extracted_path = fetch_package(package_name)
    # Step 2: Find and print the HTML/web assets
    web_assets = find_web_assets(extracted_path)
    if web_assets:
        print(f"Found web assets in {package_name}:")
        for asset in web_assets:
            print(asset)
    else:
        print(f"No web assets found in {package_name}.")
