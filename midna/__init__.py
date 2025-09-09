"""Midna - Smart pip requirements installer"""

__version__ = "1.0.0"
__author__ = "Jassem Manita"
__description__ = "Smart pip requirements installer"

from .core import main
from .installer import install_packages
from .uninstaller import uninstall_packages, check_packages_to_uninstall
from .parser import read_requirements, parse_package_name
from .checker import check_installed_packages
from .logger import setup_logging
from .discovery import auto_discover_requirements

__all__ = [
    "main",
    "install_packages",
    "uninstall_packages",
    "check_packages_to_uninstall",
    "read_requirements",
    "parse_package_name",
    "check_installed_packages",
    "setup_logging",
    "auto_discover_requirements",
]
