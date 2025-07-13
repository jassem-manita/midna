#!/usr/bin/env python3
"""
ZAP - Smart pip requirements installer

A better way to install Python packages from requirements files.
Only installs missing packages and provides clear progress feedback.

Usage:
    zap [requirements_file] [--dry-run] [--verbose] [--version] [--help]

Author: Jassem Manita
License: Apache License 2.0
Repository: https://github.com/jassem-manita/zap
"""

import argparse
import logging
import os
import subprocess  # nosec B404
import sys
from pathlib import Path
from typing import List, Set

__version__ = "0.1.0"


def setup_logging(verbose: bool = False) -> logging.Logger:
    log_dir = Path.home() / ".zap" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "zap.log"

    logger = logging.getLogger("zap")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger


def read_requirements(file_path: str) -> List[str]:
    logger = logging.getLogger("zap")
    logger.info(f"Reading requirements from: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Requirements file not found: {file_path}")
        raise FileNotFoundError(f"Requirements file '{file_path}' not found.")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        packages = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                packages.append(line)

        logger.info(f"Found {len(packages)} packages in requirements file")
        return packages

    except Exception as e:
        logger.error(f"Error reading requirements file: {e}")
        raise


def parse_package_name(requirement: str) -> str:
    separators = [">=", "<=", "==", "!=", ">", "<", "~="]

    name = requirement
    for sep in separators:
        if sep in name:
            name = name.split(sep)[0]
            break

    return name.strip()


def check_installed_packages() -> Set[str]:
    logger = logging.getLogger("zap")
    logger.info("Checking currently installed packages...")

    try:
        result = subprocess.run(  # nosec B603
            [sys.executable, "-m", "pip", "list", "--format=freeze"],
            capture_output=True,
            text=True,
            check=True,
        )

        installed = set()
        for line in result.stdout.strip().split("\n"):
            if "==" in line:
                package_name = line.split("==")[0].lower()
                installed.add(package_name)

        logger.info(f"Found {len(installed)} installed packages")
        return installed

    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to check installed packages: {e}")
        print(f"ERROR: Error checking installed packages: {e}")
        return set()


def install_packages(packages: List[str], dry_run: bool = False) -> tuple:
    logger = logging.getLogger("zap")

    if not packages:
        print("INFO: No packages to install.")
        return 0, 0

    installed = check_installed_packages()

    to_install = []
    already_installed = []

    for pkg in packages:
        package_name = parse_package_name(pkg).lower()
        if package_name in installed:
            already_installed.append(pkg)
        else:
            to_install.append(pkg)

    total_packages = len(packages)
    already_count = len(already_installed)
    to_install_count = len(to_install)

    print("INFO: Requirements Analysis:")
    print(f"   * Total packages: {total_packages}")
    print(f"   * Already installed: {already_count}")
    print(f"   * Need installation: {to_install_count}")

    if already_installed:
        print(f"\nOK: Already installed ({already_count}):")
        for pkg in already_installed:
            print(f"   * {pkg}")

    if not to_install:
        print("\nSUCCESS: All packages are already installed!")
        logger.info("All packages already installed, nothing to do")
        return total_packages, total_packages

    if dry_run:
        print(f"\nDRY RUN MODE - Would install ({to_install_count}):")
        for pkg in to_install:
            print(f"   * {pkg}")
        print("\nTIP: Run without --dry-run to actually install packages")
        logger.info(f"Dry run completed. Would install {to_install_count}")
        return 0, total_packages

    print(f"\nINSTALLING: Installing packages ({to_install_count}):")
    successful = 0

    for i, pkg in enumerate(to_install, 1):
        print(f"   [{i}/{to_install_count}] Installing {pkg}...", end=" ")
        logger.info(f"Installing package {i}/{to_install_count}: {pkg}")

        try:
            subprocess.run(  # nosec B603
                [sys.executable, "-m", "pip", "install", pkg],
                capture_output=True,
                text=True,
                check=True,
            )
            print("OK")
            successful += 1
            logger.info(f"Successfully installed: {pkg}")

        except subprocess.CalledProcessError as e:
            print("FAILED")
            error_msg = f"Failed to install {pkg}: {e}"
            print(f"      Error: {e.stderr.strip() if e.stderr else 'Unknown error'}")
            logger.error(error_msg)

    total_successful = successful + already_count
    success_rate = (total_successful / total_packages) * 100

    print("\nSUMMARY: Installation Summary:")
    print(f"   * Successfully installed: {successful}/{to_install_count}")
    print(
        f"   * Overall success rate: {total_successful}/{total_packages} "
        f"({success_rate:.1f}%)"
    )

    if successful == to_install_count:
        print("SUCCESS: All packages installed successfully!")
        logger.info("All packages installed successfully")
    else:
        failed = to_install_count - successful
        print(f"WARNING: {failed} package(s) failed to install")
        logger.warning(f"{failed} packages failed to install")

    return total_successful, total_packages


def main():
    parser = argparse.ArgumentParser(
        description="ZAP - A smarter pip requirements installer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  zap                          Install from requirements.txt
  zap requirements.txt         Install from specific file
  zap --dry-run               Preview installation from requirements.txt
  zap --verbose requirements.txt  Install with detailed logging

For more information, visit: https://github.com/jassem-manita/zap
        """,
    )

    parser.add_argument(
        "requirements_file",
        nargs="?",
        default="requirements.txt",
        help="Requirements file to install from (default: requirements.txt)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be installed without actually installing",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging output",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"ZAP {__version__}",
        help="Show version information",
    )

    args = parser.parse_args()

    logger = setup_logging(args.verbose)
    logger.info(f"ZAP {__version__} started with args: {sys.argv[1:]}")

    print(f"ZAP {__version__} - Smart Python Package Installer")
    print(f"Requirements file: {args.requirements_file}")

    if args.dry_run:
        print("Running in DRY RUN mode")

    print()

    try:
        packages = read_requirements(args.requirements_file)

        if not packages:
            print("INFO: No packages found in requirements file.")
            logger.info("No packages found in requirements file")
            return 0

        successful, total = install_packages(packages, args.dry_run)

        if successful == total:
            exit_code = 0
        else:
            exit_code = 1

        logger.info(f"ZAP completed with exit code: {exit_code}")
        return exit_code

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        logger.error(f"File not found: {e}")
        return 1

    except KeyboardInterrupt:
        print("\nWARNING: Installation interrupted by user")
        logger.info("Installation interrupted by user")
        return 130

    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        logger.error(f"Unexpected error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
