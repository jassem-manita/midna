#!/usr/bin/env python3
"""
ZAP - Python Package Operations

I got tired of pip's messy output and built this instead.
It shows you what's happening and doesn't reinstall stuff you already have.

Copyright 2025 Jassem

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import subprocess
import sys
import argparse
import os
import re
from pathlib import Path

__version__ = "1.0.0"

def read_requirements(file_path):
    """Read a requirements file and return the package names"""
    packages = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    packages.append(line)
    except FileNotFoundError:
        print(f"Can't find {file_path} - are you sure it exists?")
        return []
    except Exception as e:
        print(f"Something went wrong reading {file_path}: {e}")
        return []
    
    return packages

def check_installed_packages():
    """Figure out what packages are already installed"""
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                              capture_output=True, text=True, timeout=15) 
        if result.returncode == 0:
            installed = set()
            for line in result.stdout.split('\n')[2:]:
                if line.strip():
                    package_name = line.split()[0].lower()
                    installed.add(package_name)
            return installed
    except Exception as e:
        print(f"Couldn't check what's already installed: {e}")
    return set()

def parse_package_name(requirement):
    """Extract the package name from requirement strings"""
    name = re.split(r'[<>=!~]', requirement)[0].strip()
    return name.lower()

def dry_run_install(packages):
    """Show what would happen without actually installing anything"""
    print(f"ZAP - Python Package Operations v{__version__}")
    print("=" * 50)
    print("DRY RUN MODE - Nothing will actually be installed")
    print(f"Found {len(packages)} packages in your requirements file")
    print()
    
    installed = check_installed_packages()
    
    to_install = []
    already_installed = []
    
    for pkg in packages:
        pkg_name = parse_package_name(pkg)
        if pkg_name in installed:
            already_installed.append(pkg)
        else:
            to_install.append(pkg)
    
    if already_installed:
        print(f"Already have these ({len(already_installed)}):")
        for pkg in already_installed:
            print(f"  ✓ {pkg}")
        print()
    
    if to_install:
        print(f"Would install these ({len(to_install)}):")
        for pkg in to_install:
            print(f"  + {pkg}")
        print()
        print("To actually install them, run:")
        print(f"  zap {' '.join(sys.argv[1:]).replace('--dry-run', '').strip()}")
    else:
        print("Looks like you already have everything! 🎉")
    
    print("\nDry run complete!")

def install_packages(packages):
    """Actually install the packages for real"""
    print(f"ZAP - Python Package Operations v{__version__}")
    print("=" * 50)
    print(f"Time to install {len(packages)} packages...")
    print()
    
    installed = check_installed_packages()
    
    to_install = []
    skipped = 0
    
    for pkg in packages:
        pkg_name = parse_package_name(pkg)
        if pkg_name in installed:
            print(f"  ✓ {pkg} (already have this one)")
            skipped += 1
        else:
            to_install.append(pkg)
    
    if skipped > 0:
        print(f"\nSkipped {skipped} packages you already have")
    
    if not to_install:
        print("\nYou already have everything! Nothing to do. 🎉")
        return True
    
    print(f"\nInstalling {len(to_install)} new packages...")
    
    success_count = 0
    for i, pkg in enumerate(to_install, 1):
        print(f"  [{i}/{len(to_install)}] Installing {pkg}...")
        try:
            result = subprocess.run([
                sys.executable, '-m', 'pip', 'install', pkg
            ], capture_output=True, text=True, timeout=60)  
            
            if result.returncode == 0:
                print(f"    ✓ {pkg} installed successfully")
                success_count += 1
            else:
                error_msg = result.stderr.strip()
                if len(error_msg) > 80:  
                    error_msg = error_msg[:80] + "..."
                print(f"    ✗ {pkg} failed: {error_msg}")
        except subprocess.TimeoutExpired:
            print(f"    ✗ {pkg} took too long and timed out")
        except Exception as e:
            print(f"    ✗ {pkg} had an error: {e}")
    
    print("\n" + "=" * 50)
    print("HOW DID WE DO?")
    print("=" * 50)
    print(f"Total packages: {len(packages)}")
    print(f"Already had: {skipped}")
    print(f"Newly installed: {success_count}")
    print(f"Failed: {len(to_install) - success_count}")
    
    if to_install:
        success_rate = success_count/len(to_install)*100
        print(f"Success rate: {success_rate:.1f}%")
        if success_rate == 100:
            print("Perfect! 🎉")
        elif success_rate >= 80:
            print("Pretty good! 👍")
        else:
            print("Could be better, but that's pip for you 🤷")
    
    return success_count == len(to_install)

def main():
    """Main function - where the magic happens"""
    parser = argparse.ArgumentParser(
        description="ZAP - Python Package Operations: The installer that actually makes sense",
        prog="zap"
    )
    parser.add_argument('file', nargs='?', default='requirements.txt',
                       help='Requirements file to install from (default: requirements.txt)')
    parser.add_argument('--dry-run', action='store_true',
                       help='See what would be installed without actually doing it')
    parser.add_argument('--version', action='version', version=f'zap {__version__}')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"Can't find {args.file} - are you sure it exists?")
        print("\nHere's how to use this:")
        print("  zap                     # Install from requirements.txt")
        print("  zap my-stuff.txt        # Install from a custom file")
        print("  zap --dry-run           # See what would happen first")
        return 1
    
    packages = read_requirements(args.file)
    if not packages:
        print("Didn't find any packages to install!")
        return 1
    
    if args.dry_run:
        dry_run_install(packages)
        return 0
    else:
        success = install_packages(packages)
        return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
