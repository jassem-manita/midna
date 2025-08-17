"""Requirements file parser for ZAP"""

import logging
import os
from typing import List


def read_requirements(file_path: str) -> List[str]:
    """Read and parse requirements from a file"""
    logger = logging.getLogger("zap")
    logger.info(f"Reading requirements from: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Requirements file not found: {file_path}")
        raise FileNotFoundError(f"Requirements file '{file_path}' not found.")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        logger.error(f"Error reading requirements file: {e}")
        raise

    packages = []
    for line_num, line in enumerate(lines, 1):
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith("#"):
            continue

        # Handle -r includes (recursive requirements)
        if line.startswith("-r "):
            include_file = line[3:].strip()
            if not os.path.isabs(include_file):
                # Make relative path relative to current requirements file
                include_file = os.path.join(
                    os.path.dirname(file_path), include_file
                )

            logger.info(f"Found include: {include_file}")
            try:
                included_packages = read_requirements(include_file)
                packages.extend(included_packages)
            except FileNotFoundError:
                logger.warning(f"Included file not found: {include_file}")
                msg = (
                    f"WARNING: Included requirements file not found: "
                    f"{include_file}"
                )
                print(msg)
            continue

        # Skip other pip options
        if line.startswith("-"):
            logger.debug(f"Skipping pip option at line {line_num}: {line}")
            continue

        packages.append(line)
        logger.debug(f"Added package: {line}")

    logger.info(f"Found {len(packages)} packages in {file_path}")
    return packages


def parse_package_name(package_spec: str) -> str:
    """Extract package name from package specification"""
    import re

    # Remove comments
    if "#" in package_spec:
        package_spec = package_spec.split("#")[0].strip()

    # Extract package name (everything before version specifiers)
    # Handle cases like: package>=1.0, package==1.0, package[extra]>=1.0
    pattern = r"^([a-zA-Z0-9_-]+(?:\[[a-zA-Z0-9_,-]+\])?)"
    match = re.match(pattern, package_spec)

    if match:
        return match.group(1).split("[")[0]  # Remove extras

    # Fallback: split on common version specifiers
    for separator in [">=", "<=", "==", "!=", ">", "<", "~="]:
        if separator in package_spec:
            return package_spec.split(separator)[0].strip()

    return package_spec.strip()
