"""Midna - Smart pip requirements installer"""

__version__ = "1.0.6"
__author__ = "Jassem Manita"
__description__ = "Smart pip requirements installer"

from .checker import check_installed_packages
from .core import main
from .discovery import auto_discover_requirements
from .installer import install_packages
from .logger import setup_logging
from .parser import parse_package_name, read_requirements
from .uninstaller import check_packages_to_uninstall, uninstall_packages

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
