"""Main CLI interface for ZAP"""

import argparse
import sys

from .checker import check_installed_packages
from .installer import install_packages
from .uninstaller import uninstall_packages, check_packages_to_uninstall
from .logger import setup_logging
from .parser import read_requirements
from .discovery import auto_discover_requirements


def create_parser():
    """Create and configure the argument parser"""
    parser = argparse.ArgumentParser(
        description="ZAP - Smart pip requirements installer",
        epilog=(
            "Examples:\n"
            "  zap                    # Auto-discover requirements\n"
            "  zap file.txt           # Use specific requirements file\n"
            "  zap --dry-run          # Preview auto-discovered packages\n"
            "  zap file.txt --dry-run # Preview specific file packages"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "requirements_file",
        nargs="?",
        help="Path to requirements.txt file (optional - will auto-discover)"
    )
    parser.add_argument(
        "--uninstall",
        "-u",
        action="store_true",
        help="Uninstall packages instead of installing them",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Show what would be installed/uninstalled without doing it",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s 0.1.0"
    )
    return parser


def main():
    """Main entry point for ZAP"""
    parser = create_parser()
    args = parser.parse_args()
    logger = setup_logging(args.verbose)
    logger.info("ZAP started")

    try:
        # Determine how to get packages
        if args.requirements_file:
            # Traditional mode: use specified file
            packages = read_requirements(args.requirements_file)
            source_info = f"file: {args.requirements_file}"
            logger.info(f"Using specified file: {args.requirements_file}")
        else:
            # Auto-discovery mode
            print("🔍 Auto-discovering requirements...")
            packages, discovery_method = auto_discover_requirements(".")
            source_info = discovery_method
            logger.info(f"Auto-discovery used: {discovery_method}")
        
        if not packages:
            if args.requirements_file:
                print("No packages found in requirements file.")
            else:
                print("No packages discovered in current directory.")
                print("\nTip: You can:")
                print("  • Create a requirements.txt file")
                print("  • Run 'zap <filename>' to specify a file")
                print("  • Add import statements to your Python files")
            return 0
            
        print(f"📦 Found {len(packages)} packages ({source_info})")
        
        # Show packages that were found
        if args.verbose or not args.requirements_file:
            print("\nDiscovered packages:")
            for package in packages:
                print(f"  • {package}")

        if args.uninstall:
            # Handle uninstall mode
            if args.requirements_file:
                found_packages, not_found_packages = (
                    check_packages_to_uninstall(args.requirements_file)
                )
            else:
                # For auto-discovered packages, create temp file
                import tempfile
                with tempfile.NamedTemporaryFile(
                    mode='w', suffix='.txt', delete=False
                ) as temp_file:
                    temp_file.write('\n'.join(packages))
                    temp_path = temp_file.name
                
                try:
                    found_packages, not_found_packages = (
                        check_packages_to_uninstall(temp_path)
                    )
                finally:
                    import os
                    os.unlink(temp_path)
            
            if not_found_packages:
                print(
                    f"\n❌ Not installed ({len(not_found_packages)} packages):"
                )
                for package in not_found_packages:
                    print(f"  - {package}")
            if not found_packages:
                print("\n✅ No packages to uninstall (none are installed)!")
                return 0
            print(f"\n🗑️  Will uninstall ({len(found_packages)} packages):")
            for package in found_packages:
                print(f"  - {package}")
            
            # Create temp file for uninstaller
            import tempfile
            with tempfile.NamedTemporaryFile(
                mode='w', suffix='.txt', delete=False
            ) as temp_file:
                temp_file.write('\n'.join(found_packages))
                temp_path = temp_file.name
            
            try:
                exit_code = uninstall_packages(temp_path, args.dry_run)
            finally:
                import os
                os.unlink(temp_path)
            
            return exit_code
        else:
            # Handle install mode
            missing_packages, already_installed = check_installed_packages(
                packages
            )
            if already_installed:
                print(
                    f"\n✅ Already installed ({len(already_installed)} "
                    f"packages):"
                )
                for package in already_installed:
                    print(f"  + {package}")
            if not missing_packages:
                print("\n🎉 All packages are already installed!")
                return 0
            print(f"\n⬇️  Will install ({len(missing_packages)} packages):")
            for package in missing_packages:
                print(f"  - {package}")
            exit_code = install_packages(missing_packages, args.dry_run)
            return exit_code
            
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return 1
    except KeyboardInterrupt:
        operation = "Uninstallation" if args.uninstall else "Installation"
        print(f"\nWARNING: {operation} interrupted by user")
        return 130
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
