# ZAP - Python Package Operations

A smarter Python package installer.

> ** Current Status**: ZAP is ready to use! PyPI publication coming soon.

## Overview

ZAP improves upon pip install -r requirements.txt by providing preview functionality, skipping already installed packages, and offering clear progress feedback.

## Features

- **Dry-run mode**: Preview installations before executing
- **Smart detection**: Skip packages that are already installed
- **Clear progress**: Readable output with installation summaries  
- **Error handling**: Continue installing other packages if one fails
- **Zero configuration**: Works with existing requirements.txt files

## Quick Start

### Install ZAP

`ash
# Clone and install locally
git clone https://github.com/jassem-manita/zap.git
cd zap
pip install .
`

### Basic Usage

`ash
# Install from requirements.txt (preview first)
zap --dry-run

# Actually install the packages
zap

# Install from a custom requirements file
zap my-packages.txt
`

## Installation Methods

### Method 1: Install as Command (Recommended)

`ash
# Clone the repository
git clone https://github.com/jassem-manita/zap.git
cd zap

# Install ZAP globally
pip install .

# Now use anywhere
zap --help
zap --dry-run
zap
`

### Method 2: Direct Script Usage

`ash
# Download just the script
curl -O https://raw.githubusercontent.com/jassem-manita/zap/main/zap.py

# Run directly
python zap.py --help
python zap.py --dry-run
python zap.py
`

## Command Line Options

`	ext
usage: zap [-h] [--dry-run] [--version] [file]

positional arguments:
  file        Requirements file to install from (default: requirements.txt)

optional arguments:
  -h, --help  show this help message and exit
  --dry-run   See what would be installed without actually doing it
  --version   show program's version number and exit
`

## Examples

`ash
# Preview what would be installed
zap --dry-run

# Install everything in requirements.txt
zap

# Install from a specific file
zap dev-requirements.txt

# Check version
zap --version
`

## Sample Output

`	ext
ZAP - Python Package Operations v1.0.0
==================================================
DRY RUN MODE - Nothing will actually be installed
Found 3 packages in your requirements file

Already have these (1):
   requests>=2.25.0

Would install these (2):
  + numpy>=1.21.0
  + pandas>=1.3.0

To actually install them, run:
  zap 

Dry run complete!
`

## Why ZAP?

- **Preview before installing**: See what will happen with --dry-run
- **Skip duplicates**: Won't reinstall packages you already have
- **Clear progress**: Shows exactly what's happening, not pip's verbose output
- **Simple**: Just works with your existing requirements.txt files
- **Fast**: Only installs what you actually need

## Requirements

- Python 3.6+
- pip (comes with Python)

## How It Works

1. **Reads** your requirements.txt (or specified file)
2. **Checks** what packages you already have installed
3. **Shows** you what will be installed (in dry-run mode)
4. **Installs** only the missing packages
5. **Reports** success/failure summary

## License

Licensed under the Apache License, Version 2.0. See LICENSE for details.

## Author

Created by Jassem - because pip's output was driving me crazy.

---

**Happy installing!** 